"""脱敏测试。"""
from contextloom.security.redact import redact


def test_redact_email():
    assert redact("联系 a@b.com") == "联系 [EMAIL]"


def test_redact_phone():
    assert redact("电话 13812345678") == "电话 [PHONE]"
