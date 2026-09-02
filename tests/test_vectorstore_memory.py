"""内存向量后端测试。"""
import pytest

from contextloom.core.models import Chunk
from contextloom.vectorstore.memory import MemoryStore


@pytest.mark.asyncio
async def test_add_search():
    store = MemoryStore()
    chunks = [Chunk(id=f"c{i}", document_id="d", collection="col",
                    text=f"文本{i}", embedding=[1.0, 0.0] if i == 0 else [0.0, 1.0])
              for i in range(3)]
    await store.add(chunks, "col")
    assert await store.count("col") == 3
    res = await store.search([1.0, 0.0], "文本0", "col", 2)
    assert res[0].chunk_id == "c0"


@pytest.mark.asyncio
async def test_delete():
    store = MemoryStore()
    await store.add([Chunk(id="x", document_id="d", collection="c", text="t")], "c")
    await store.delete_collection("c")
    assert await store.count("c") == 0
