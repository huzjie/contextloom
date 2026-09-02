"""向量化工厂测试。"""
from contextloom.config.settings import Settings
from contextloom.embedding.factory import get_embedder


def test_fallback():
    s = Settings(embed_allow_hash_fallback=True, _env_file=None)
    e = get_embedder(s)
    assert e is not None
