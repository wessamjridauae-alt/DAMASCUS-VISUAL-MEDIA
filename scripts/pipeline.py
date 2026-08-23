from __future__ import annotations
import argparse,json
from datetime import date
from pathlib import Path
from common import ROOT,load_json,idempotency_key,append_jsonl,utcnow
from discover_topics import discover
from render_preview import render
from quality_control import inspect

def run(slot="A",dry_run=True):
    cfg=load_json("config/publishing.json"); candidates=discover(dry_run)
    floor=85 if slot=="C" else 75
    chosen=next((x for x in sorted(candidates,key=lambda x:x["total_score"],reverse=True) if x["total_score"]>=floor),None)
    if not chosen:return {"status":"skipped","reason":"no_candidate_above_threshold"}
    day=str(date.today());key=idempotency_key(day,slot,chosen["id"])
    out=ROOT/"output"/day/key;out.mkdir(parents=True,exist_ok=True)
    render(out/"carousel-01.png",(1080,1350),"دمشق… بهويّة تُعرف من النظرة الأولى","دفء الحجر، عمق الظلال، وذهبٌ هادئ","DAMASCUS SIGNATURE / 01")
    render(out/"story-01.png",(1080,1920),"اكتشف دمشق بصورة مختلفة","معاينة الهوية البصرية الأولى","NEW STORY")
    qa={"carousel":inspect(out/"carousel-01.png",(1080,1350)),"story":inspect(out/"story-01.png",(1080,1920))}
    result={"status":"preview_ready","dry_run":dry_run,"publishable":False,"idempotency_key":key,"slot":slot,"topic":chosen,"qa":qa,"created_at":utcnow(),"output":str(out.relative_to(ROOT))}
    (out/"manifest.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    return result
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--slot",default="A");ap.add_argument("--live",action="store_true");a=ap.parse_args()
    print(json.dumps(run(a.slot,not a.live),ensure_ascii=False,indent=2))
