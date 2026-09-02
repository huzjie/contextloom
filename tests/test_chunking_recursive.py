"""递归分块器测试。"""
from contextloom.chunking.recursive import RecursiveChunker


def test_short_text():
    c = RecursiveChunker(chunk_size=1000)
    assert c.split("短文本") == ["短文本"]


def test_long_split():
    c = RecursiveChunker(chunk_size=20, overlap=5)
    text = "。" .join(["句子%d" % i for i in range(50)])
    chunks = c.split(text)
    assert len(chunks) > 1
    assert all(len(x) <= 25 for x in chunks)


def test_empty():
    assert RecursiveChunker().split("   ") == []
