"""SQLite 后端测试。"""
import pytest

from contextloom.core.models import Chunk
from contextloom.vectorstore.sqlite import SQLiteStore


@pytest.mark.asyncio
async def test_roundtrip(tmp_path):
    store = SQLiteStore(tmp_path, dim=2)
    chunks = [Chunk(id="c0", document_id="d", collection="col", text="苹果手机",
                    embedding=[1.0, 0.0])]
    await store.add(chunks, "col")
    assert await store.count("col") == 1
    res = await store.search([1.0, 0.0], "苹果", "col", 1)
    assert len(res) == 1


@pytest.mark.asyncio
async def test_delete(tmp_path):
    store = SQLiteStore(tmp_path, dim=2)
    await store.add([Chunk(id="x", document_id="d", collection="c", text="t",
                           embedding=[1.0, 0.0])], "c")
    await store.delete_collection("c")
    assert await store.count("c") == 0
