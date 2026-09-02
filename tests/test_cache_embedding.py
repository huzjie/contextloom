"""向量缓存测试。"""
from contextloom.cache.embedding_cache import EmbeddingCache


def test_cache():
    c = EmbeddingCache()
    assert c.get("x") is None
    c.set("x", [1.0, 2.0])
    assert c.get("x") == [1.0, 2.0]
