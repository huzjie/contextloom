"""输入清理工具。"""

from __future__ import annotations

import re

_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def sanitize_text(text: str, max_length: int = 1_000_000) -> str:
    """去除控制字符并限制长度。"""
    cleaned = _CONTROL.sub("", text)
    return cleaned[:max_length]
