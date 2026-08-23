from __future__ import annotations
import hashlib,json,os
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def load_json(rel):
    return json.loads((ROOT/rel).read_text(encoding="utf-8"))
def append_jsonl(rel,row):
    p=ROOT/rel;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("a",encoding="utf-8") as f:f.write(json.dumps(row,ensure_ascii=False)+"\n")
def idempotency_key(date,slot,topic):
    return hashlib.sha256(f"{date}|{slot}|{topic}".encode()).hexdigest()[:24]
def utcnow():
    return datetime.now(timezone.utc).isoformat()
def require_review_guard(cfg):
    live=os.getenv("AUTOPUBLISH_ENABLED","false").lower()=="true"
    return live and bool(cfg.get("autopublish_enabled")) and cfg.get("mode")=="AUTOPUBLISH"
