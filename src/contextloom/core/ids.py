"""稳定 ID 生成工具。"""

from __future__ import annotations

import hashlib
import uuid


def short_id(prefix: str = "") -> str:
    raw = uuid.uuid4().hex[:12]
    return f"{prefix}_{raw}" if prefix else raw


def content_hash(text: str, length: int = 16) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:length]


def doc_id(source: str) -> str:
    return "doc_" + content_hash(source, 16)


def chunk_id(document_id: str, index: int) -> str:
    return f"{document_id}_c{index:05d}"
