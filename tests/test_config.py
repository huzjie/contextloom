"""配置系统测试。"""
import pytest


def test_settings_defaults():
    from contextloom.config.settings import Settings
    s = Settings(llm_backend="mock", vector_backend="memory",
                 embed_allow_hash_fallback=True, _env_file=None)
    assert s.llm_backend == "mock"
    assert s.port == 8000
    assert s.chunk_overlap < s.chunk_size


def test_settings_validation():
    from contextloom.config.settings import Settings
    with pytest.raises(Exception):
        Settings(port=0, _env_file=None)


def test_load_settings_cached():
    from contextloom.config.settings import load_settings
    a = load_settings()
    b = load_settings()
    assert a is b
