from __future__ import annotations
import os,requests,json
def run():
    needed=["META_ACCESS_TOKEN","INSTAGRAM_USER_ID","META_GRAPH_API_VERSION","MEDIA_STORAGE_BUCKET","MEDIA_CDN_BASE_URL"]
    missing=[x for x in needed if not os.getenv(x)]
    if missing:return {"status":"not_configured","missing":missing}
    base=f"https://graph.facebook.com/{os.environ['META_GRAPH_API_VERSION']}"
    r=requests.get(f"{base}/{os.environ['INSTAGRAM_USER_ID']}",params={"fields":"id,username","access_token":os.environ["META_ACCESS_TOKEN"]},timeout=30)
    return {"status":"ok" if r.ok else "error","http_status":r.status_code}
if __name__=="__main__":print(json.dumps(run(),indent=2))
