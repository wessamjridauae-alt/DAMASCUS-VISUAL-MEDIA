from __future__ import annotations
from urllib.parse import urlparse

REQUIRED=("url","source_type","accessed_at","claims","confidence")
def verify_record(record):
    errors=[]
    for s in record.get("sources",[]):
        errors += [f"missing:{k}" for k in REQUIRED if not s.get(k)]
        if s.get("url") and urlparse(s["url"]).scheme not in ("http","https"): errors.append("invalid_url")
    rights=record.get("image_rights",{})
    for k in ("source_url","creator","license","attribution_required"):
        if k not in rights: errors.append(f"image_rights_missing:{k}")
    if not record.get("sources"): errors.append("no_sources")
    return {"passed":not errors,"errors":errors}
