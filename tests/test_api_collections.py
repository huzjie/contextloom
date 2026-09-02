"""知识库路由测试。"""
from fastapi.testclient import TestClient

from contextloom.api.app import create_app


def test_list_collections():
    c = TestClient(create_app())
    r = c.get("/collections")
    assert r.status_code == 200
    assert "collections" in r.json()
