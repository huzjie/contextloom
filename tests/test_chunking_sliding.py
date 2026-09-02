"""滑动窗口分块器测试。"""
from contextloom.chunking.sliding import SlidingChunker


def test_sliding():
    c = SlidingChunker(chunk_size=10, overlap=2)
    text = "abcdefghijklmnopqrstuvwxyz"
    chunks = c.split(text)
    assert chunks[0] == text[:10]
    assert chunks[1] == text[8:18]


def test_empty():
    assert SlidingChunker().split("") == []
