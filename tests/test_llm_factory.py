"""LLM 工厂测试。"""
import pytest

from contextloom.config.settings import Settings
from contextloom.llm.factory import create_backend


def test_mock():
    s = Settings(llm_backend="mock", _env_file=None)
    assert create_backend(s).name == "mock"


def test_ollama():
    s = Settings(llm_backend="ollama", _env_file=None)
    assert create_backend(s).name == "ollama"


def test_unknown():
    with pytest.raises(ValueError):
        create_backend(Settings(llm_backend="bad", _env_file=None))
