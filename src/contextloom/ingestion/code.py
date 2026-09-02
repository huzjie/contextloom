"""代码目录/仓库解析器。"""

from __future__ import annotations

from pathlib import Path

from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import register_parser

_CODE_EXT = {".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".rs", ".java", ".c",
             ".cpp", ".h", ".sh", ".sql", ".yaml", ".yml", ".toml", ".json", ".vue"}
_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}


@register_parser(".repo", ".code")
class CodeRepoParser(BaseParser):
    extensions = (".repo", ".code")

    async def parse(self, path: str | Path) -> ParsedDocument:
        root = Path(path)
        if root.is_file():
            root = root.parent
        parts: list[str] = []
        for file in sorted(root.rglob("*")):
            if not file.is_file() or file.suffix.lower() not in _CODE_EXT:
                continue
            if any(seg in _SKIP_DIRS for seg in file.parts):
                continue
            rel = file.relative_to(root)
            try:
                content = file.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            parts.append(f"===== {rel} =====\n{content}")
        return ParsedDocument(title=root.name, text="\n\n".join(parts),
                              source=str(root), metadata={"format": "code", "files": len(parts)})
