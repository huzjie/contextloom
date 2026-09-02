# 插件开发

## 自定义解析器

```python
from contextloom.ingestion.base import BaseParser, ParsedDocument
from contextloom.ingestion.registry import register_parser

@register_parser(".myext")
class MyParser(BaseParser):
    async def parse(self, path):
        return ParsedDocument(title="x", text="...", source=str(path))
```
