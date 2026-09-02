"""分块器基类测试。"""
from contextloom.chunking.recursive import RecursiveChunker


def test_make_chunks():
    c = RecursiveChunker(chunk_size=100)
    chunks = c.make_chunks("这是内容。", "doc1", "coll")
    assert len(chunks) >= 1
    assert all(ch.document_id == "doc1" for ch in chunks)
    assert all(ch.collection == "coll" for ch in chunks)
