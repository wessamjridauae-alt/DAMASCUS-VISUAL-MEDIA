from __future__ import annotations
import os,requests
METRICS="reach,likes,comments,saved,shares,profile_visits,follows"
def collect(media_id):
    v=os.environ["META_GRAPH_API_VERSION"];t=os.environ["META_ACCESS_TOKEN"]
    r=requests.get(f"https://graph.facebook.com/{v}/{media_id}/insights",params={"metric":METRICS,"access_token":t},timeout=30);r.raise_for_status();return r.json()
