"""ID 生成测试。"""
from contextloom.core.ids import chunk_id, content_hash, doc_id, short_id


def test_short_id():
    assert short_id("doc").startswith("doc_")
    assert len(short_id("x")) == 14


def test_content_hash_stable():
    assert content_hash("abc") == content_hash("abc")
    assert content_hash("abc") != content_hash("abd")


def test_doc_chunk_id():
    did = doc_id("file.txt")
    assert did.startswith("doc_")
    assert chunk_id(did, 3).endswith("_c00003")
