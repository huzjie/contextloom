"""文档摄入路由测试。"""
from fastapi.testclient import TestClient

from contextloom.api.app import create_app


def test_ingest_bad():
    c = TestClient(create_app())
    r = c.post("/documents/ingest", json={"source": "/no/such.md", "collection": "c"})
    assert r.status_code in (400, 500)
