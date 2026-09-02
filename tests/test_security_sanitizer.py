"""输入清理测试。"""
from contextloom.security.sanitizer import sanitize_text


def test_control_chars():
    assert sanitize_text("a\x00b") == "ab"


def test_max_length():
    assert len(sanitize_text("x" * 100, max_length=10)) == 10
