#!/usr/bin/env python3
# runner.py — v2-validation 배치 러너 (codex-imagegen 스킬 러너의 레이스-세이프 적응판)
#
# codex exec를 N개 병렬 스폰해 레코드당 이미지 1장을 $imagegen으로 생성하고,
# ~/.codex/generated_images/ 에 떨어진 PNG를 claimed-집합 + 원자적 move로 레이스 없이 회수한다.
#
# 실행:
#   python3 runner.py [expA_text.jsonl expB_compliance.jsonl expC_layout.jsonl]
#     (인자 없으면 위 3개 파일 기본)
#   PARALLEL=auto(기본: min(작업수, MAX(기본 6)))  |  PARALLEL=4 수동 고정
#   TIMEOUT=300 (초, 2048/high 헤드룸 포함)   DRY_RUN=1 (스폰 없이 계획만 출력)
#
# 프로토콜 (runs.log):
#   SAVED: <id> <output_path>       — 회수 성공
#   FAILED: <id> reason=<...>       — 실패. reason=refusal:* 이면 모더레이션 거부 (Exp B 1차 지표)
#   SKIP: <id>                      — output_path 이미 존재 (resume)
#   DONE: ok=<n> fail=<n> skip=<n> total=<n>
#
# resume: output_path가 이미 있으면 스킵 — 중단 후 재실행하면 남은 것만 처리.
import json, os, re, shutil, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUTBASE = Path(os.environ.get("OUTDIR", str(BASE)))
LOG = BASE / "runs.log"
TIMEOUT = int(os.environ.get("TIMEOUT", "300"))
DRY_RUN = os.environ.get("DRY_RUN", "") not in ("", "0")
CODEX_IMG = Path.home() / ".codex" / "generated_images"
DEFAULT_FILES = ["expA_text.jsonl", "expB_compliance.jsonl", "expC_layout.jsonl"]
# 거부 감지 — codex 출력에 아래 패턴이 보이고 PNG가 없으면 FAILED reason=refusal:*
REFUSAL_RE = re.compile(
    r"rejected|safety|content policy|content_policy|moderation|"
    r"unable to generate|cannot generate|can't generate", re.I)

_loglock = threading.Lock()
def log(line):
    with _loglock:
        with LOG.open("a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%S')} {line}\n")
    print(line, flush=True)

# ── 레이스-세이프 회수: claimed 집합 + 락 (스킬 §3/§4 — 전역 최신 1장 로직의 레이스 수정) ──
_claim_lock = threading.Lock()
_claimed = set()
def newest_unclaimed(after_ts):
    with _claim_lock:
        best = None
        if CODEX_IMG.exists():
            for sess in CODEX_IMG.iterdir():
                if not sess.is_dir():
                    continue
                for png in sess.glob("ig_*.png"):
                    p = str(png)
                    if p in _claimed:
                        continue
                    try:
                        m = png.stat().st_mtime
                    except OSError:
                        continue
                    if m > after_ts and (best is None or m > best[1]):
                        best = (png, m)
        if best:
            _claimed.add(str(best[0]))
            return best[0]
        return None

def run_one(rec):
    rid = rec["id"]
    out = OUTBASE / rec["output_path"]
    if out.exists():
        return (rid, "skip", "")
    # 스킬 §1 권장 invocation 템플릿 + 레코드의 ar/size/quality
    instr = (f"Use $imagegen to generate ONE image.\n"
             f"Aspect ratio: {rec.get('ar', '2:3')}\n"
             f"Size: {rec.get('size', '1024x1536')}\n"
             f"Quality: {rec.get('quality', 'high')}\n"
             f"Prompt: {rec['full_prompt']}\n"
             f"After generation, do NOT run any shell commands. Just generate and end your turn.")
    if DRY_RUN:
        return (rid, "dry", rec["output_path"])
    before = time.time() - 1
    try:
        r = subprocess.run(
            ["codex", "exec", "--skip-git-repo-check",
             "--dangerously-bypass-approvals-and-sandbox", instr],
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=TIMEOUT, text=True)
    except subprocess.TimeoutExpired:
        return (rid, "fail", "timeout")
    except FileNotFoundError:
        return (rid, "fail", "codex-cli-not-found")
    combined = (r.stdout or "") + "\n" + (r.stderr or "")
    # PNG 회수 대기 (codex가 파일을 다 쓰는 지연 흡수)
    deadline = time.time() + 30
    src = None
    while time.time() < deadline:
        src = newest_unclaimed(before)
        if src:
            break
        time.sleep(1)
    if not src:
        m = REFUSAL_RE.search(combined)
        reason = f"refusal:{m.group(0).strip().lower().replace(' ', '-')}" if m else "no-image"
        return (rid, "fail", reason)
    # 워커별 임시 파일 → 같은 파일시스템 내 원자적 rename
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.parent / f".{out.name}.{os.getpid()}.{threading.get_ident()}.part"
    shutil.move(str(src), str(tmp))
    os.replace(tmp, out)
    return (rid, "ok", rec["output_path"])

def load_records(paths):
    records, seen = [], set()
    for p in paths:
        fp = Path(p) if os.path.isabs(p) else BASE / p
        for i, line in enumerate(fp.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            rec = json.loads(line)  # 사전 검증 전제 — 여기서 죽으면 jsonl부터 고칠 것
            if rec["id"] in seen:
                raise SystemExit(f"duplicate id across inputs: {rec['id']} ({fp}:{i})")
            seen.add(rec["id"])
            records.append(rec)
    return records

def main():
    files = sys.argv[1:] or DEFAULT_FILES
    records = load_records(files)
    todo = [r for r in records if not (OUTBASE / r["output_path"]).exists()]
    skipped = len(records) - len(todo)
    par_env = os.environ.get("PARALLEL", "auto")
    if par_env.isdigit():
        workers = max(1, int(par_env))
    else:  # auto: 작업 수에 맞추되 기본 상한 6 (MAX로 override)
        workers = max(1, min(len(todo) or 1, int(os.environ.get("MAX", "6"))))
    log(f"START: files={','.join(files)} total={len(records)} todo={len(todo)} "
        f"skip={skipped} workers={workers} timeout={TIMEOUT}s dry_run={int(DRY_RUN)}")
    for r in records:
        if (OUTBASE / r["output_path"]).exists():
            log(f"SKIP: {r['id']}")
    ok = fail = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_one, r): r["id"] for r in todo}
        for f in as_completed(futs):
            rid, status, detail = f.result()
            if status == "ok":
                ok += 1
                log(f"SAVED: {rid} {detail}")
            elif status == "dry":
                ok += 1
                log(f"DRY: {rid} -> {detail}")
            elif status == "skip":
                skipped += 1
                log(f"SKIP: {rid}")
            else:
                fail += 1
                log(f"FAILED: {rid} reason={detail}")
    log(f"DONE: ok={ok} fail={fail} skip={skipped} total={len(records)} "
        f"elapsed={(time.time() - t0) / 60:.1f}min")
    return 0 if fail == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
