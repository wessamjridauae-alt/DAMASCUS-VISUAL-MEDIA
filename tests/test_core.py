from scripts.common import idempotency_key,load_json,require_review_guard
from scripts.quality_control import inspect
def test_idempotency_is_stable():
    assert idempotency_key("2026-08-23","A","x")==idempotency_key("2026-08-23","A","x")
def test_review_mode_blocks_publish(monkeypatch):
    monkeypatch.setenv("AUTOPUBLISH_ENABLED","true")
    assert require_review_guard(load_json("config/publishing.json")) is False
def test_brand_version():
    assert load_json("config/brand.json")["version"]=="DAMASCUS_SIGNATURE_V1"
