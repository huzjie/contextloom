"""解析器基类。"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ParsedDocument:
    title: str = ""
    text: str = ""
    headings: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    source: str = ""


class BaseParser(ABC):
    extensions: tuple[str, ...] = ()

    @abstractmethod
    async def parse(self, path: str | Path) -> ParsedDocument:
        ...

    @staticmethod
    def _read_text(path: str | Path, encoding: str = "utf-8") -> str:
        return Path(path).read_text(encoding=encoding, errors="ignore")
