"""哈希向量化测试。"""
import pytest

from contextloom.embedding.hash_embedder import HashEmbedder


@pytest.mark.asyncio
async def test_embed():
    e = HashEmbedder(dim=64)
    vecs = await e.embed(["你好世界", "你好世界", "完全不同"])
    assert len(vecs) == 3
    assert vecs[0] == vecs[1]
    assert vecs[0] != vecs[2]
    assert len(vecs[0]) == 64
