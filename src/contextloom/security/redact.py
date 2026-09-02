"""敏感信息脱敏。"""

from __future__ import annotations

import re

_PATTERNS = [
    (re.compile(r"\b\d{15,19}\b"), "[CARD]"),
    (re.compile(r"\b1[3-9]\d{9}\b"), "[PHONE]"),
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "[EMAIL]"),
]


def redact(text: str) -> str:
    for pattern, repl in _PATTERNS:
        text = pattern.sub(repl, text)
    return text
