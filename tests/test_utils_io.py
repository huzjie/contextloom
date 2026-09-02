"""IO 工具测试。"""
from contextloom.utils.io import read_json, write_json


def test_roundtrip(tmp_path):
    p = tmp_path / "a.json"
    write_json(p, {"k": "v"})
    assert read_json(p)["k"] == "v"
