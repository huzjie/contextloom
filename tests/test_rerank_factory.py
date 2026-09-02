"""重排工厂测试。"""
from contextloom.config.settings import Settings
from contextloom.rerank.factory import get_reranker


def test_get():
    s = Settings(rerank_enabled=False, _env_file=None)
    assert get_reranker(s) is not None
