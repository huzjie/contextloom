"""哈希工具。"""

from __future__ import annotations

import hashlib


def md5(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def short_hash(text: str, length: int = 12) -> str:
    return sha256(text)[:length]
