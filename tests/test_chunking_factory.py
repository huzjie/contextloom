"""分块器工厂测试。"""
import pytest

from contextloom.chunking.factory import get_chunker


def test_get_each_strategy():
    for name in ["recursive", "semantic", "code", "sliding"]:
        assert get_chunker(name) is not None


def test_unknown():
    with pytest.raises(ValueError):
        get_chunker("nope")
