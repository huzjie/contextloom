"""健康检查路由测试。"""
from fastapi.testclient import TestClient

from contextloom.api.app import create_app


def test_health():
    c = TestClient(create_app())
    r = c.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
