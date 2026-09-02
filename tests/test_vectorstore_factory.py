"""向量后端工厂测试。"""
import pytest

from contextloom.config.settings import Settings
from contextloom.vectorstore.factory import create_store


def test_memory(tmp_path):
    s = Settings(vector_backend="memory", _env_file=None)
    assert create_store(s).name == "memory"


def test_sqlite(tmp_path):
    s = Settings(vector_backend="sqlite", data_dir=tmp_path, _env_file=None)
    assert create_store(s).name == "sqlite"


def test_unknown():
    with pytest.raises(ValueError):
        create_store(Settings(vector_backend="bad", _env_file=None))
