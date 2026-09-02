"""模型信息路由测试。"""
from fastapi.testclient import TestClient

from contextloom.api.app import create_app


def test_models():
    c = TestClient(create_app())
    r = c.get("/models")
    assert r.status_code == 200
    assert "llm_backend" in r.json()
