"""代码分块器测试。"""
from contextloom.chunking.code import CodeChunker


def test_function_split():
    c = CodeChunker(chunk_size=200)
    code = "def a():\n    pass\n\ndef b():\n    pass\n"
    chunks = c.split(code)
    assert len(chunks) >= 2


def test_empty():
    assert CodeChunker().split("") == []
