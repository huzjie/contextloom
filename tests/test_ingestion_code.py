"""代码解析器测试。"""
import pytest

from contextloom.ingestion.code import CodeRepoParser


@pytest.mark.asyncio
async def test_parse(tmp_path):
    (tmp_path / "a.py").write_text("print('hi')\n", encoding="utf-8")
    doc = await CodeRepoParser().parse(tmp_path)
    assert "a.py" in doc.text
    assert doc.metadata["files"] == 1
