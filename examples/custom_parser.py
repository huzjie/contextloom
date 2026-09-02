"""示例：自定义解析器。"""
from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import register_parser


@register_parser(".myext")
class MyParser(BaseParser):
    async def parse(self, path):
        return ParsedDocument(title="demo", text="自定义内容", source=str(path))
