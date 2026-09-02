"""解析器注册表。"""

from __future__ import annotations

from pathlib import PurePath

from contextloom.ingestion.base import BaseParser

_REGISTRY: dict[str, BaseParser] = {}


def register_parser(*extensions: str):
    def decorator(cls: type[BaseParser]) -> type[BaseParser]:
        instance = cls()
        for ext in extensions:
            _REGISTRY[ext.lower()] = instance
        return cls
    return decorator


def get_parser(ext_or_path: str) -> BaseParser | None:
    ext = ext_or_path.lower()
    if "/" in ext or "\\" in ext:
        ext = PurePath(ext_or_path).suffix.lower()
    return _REGISTRY.get(ext)


def supported_extensions() -> list[str]:
    return sorted(_REGISTRY)


# 触发注册
from contextloom.ingestion import (  # noqa: E402,F401
    code, docx, html, markdown, pdf, text, url,
)
