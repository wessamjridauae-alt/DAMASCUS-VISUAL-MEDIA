from __future__ import annotations
import argparse,os,requests
from common import load_json,require_review_guard

def publish_carousel(children,caption):
    cfg=load_json("config/publishing.json")
    if not require_review_guard(cfg): raise SystemExit("PUBLISH BLOCKED: review guard is active")
    token=os.environ["META_ACCESS_TOKEN"]; ig=os.environ["INSTAGRAM_USER_ID"]; ver=os.environ["META_GRAPH_API_VERSION"]
    base=f"https://graph.facebook.com/{ver}"
    child_ids=[]
    for url in children:
      r=requests.post(f"{base}/{ig}/media",data={"image_url":url,"is_carousel_item":"true","access_token":token},timeout=60);r.raise_for_status();child_ids.append(r.json()["id"])
    r=requests.post(f"{base}/{ig}/media",data={"media_type":"CAROUSEL","children":",".join(child_ids),"caption":caption,"access_token":token},timeout=60);r.raise_for_status()
    creation=r.json()["id"];p=requests.post(f"{base}/{ig}/media_publish",data={"creation_id":creation,"access_token":token},timeout=60);p.raise_for_status();return p.json()
if __name__=="__main__":
    raise SystemExit("Use pipeline integration; direct CLI publishing is intentionally disabled.")
