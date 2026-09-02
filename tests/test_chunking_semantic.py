"""语义分块器测试。"""
from contextloom.chunking.semantic import SemanticChunker


def test_sentence_grouping():
    c = SemanticChunker(chunk_size=100)
    text = "这是第一句。这是第二句。这是第三句。"
    chunks = c.split(text)
    assert len(chunks) >= 1
    assert "。" in chunks[0]


def test_empty():
    assert SemanticChunker().split(" ") == []
