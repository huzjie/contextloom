"""BM25 重排测试。"""
import pytest

from contextloom.core.models import SearchResult
from contextloom.rerank.bm25 import BM25Reranker


@pytest.mark.asyncio
async def test_rerank():
    r = BM25Reranker()
    rs = [
        SearchResult(chunk_id="a", document_id="d", text="苹果手机很贵", score=0.5),
        SearchResult(chunk_id="b", document_id="d", text="香蕉很便宜", score=0.9),
    ]
    out = await r.rerank("苹果", rs)
    assert out[0].chunk_id == "a"


@pytest.mark.asyncio
async def test_empty():
    r = BM25Reranker()
    assert await r.rerank("q", []) == []
