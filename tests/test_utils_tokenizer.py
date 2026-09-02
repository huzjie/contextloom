"""token 估算测试。"""
from contextloom.utils.tokenizer import estimate_tokens, truncate_to_tokens


def test_estimate():
    assert estimate_tokens("你好") == 2
    assert estimate_tokens("abcd") == 1


def test_truncate():
    t = truncate_to_tokens("你好世界" * 100, budget=10)
    assert estimate_tokens(t) <= 10
