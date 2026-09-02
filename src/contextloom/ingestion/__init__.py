"""文档摄入层。"""
from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import get_parser

__all__ = ["BaseParser", "ParsedDocument", "get_parser"]
