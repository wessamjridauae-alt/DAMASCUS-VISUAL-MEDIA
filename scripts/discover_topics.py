from __future__ import annotations
import argparse,json,os
from pathlib import Path
from common import ROOT,load_json

def discover(dry_run=True):
    if dry_run:
        return load_json("data/fixtures/topic-candidates.json")
    from openai import OpenAI
    client=OpenAI()
    model=os.getenv("OPENAI_DISCOVERY_MODEL","gpt-5.6-luna")
    prompt=(ROOT/"prompts/discovery.md").read_text(encoding="utf-8")
    r=client.responses.create(model=model,tools=[{"type":"web_search"}],input=prompt)
    return json.loads(r.output_text)
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--live",action="store_true");a=ap.parse_args()
    print(json.dumps(discover(not a.live),ensure_ascii=False,indent=2))
