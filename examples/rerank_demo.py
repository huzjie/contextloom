"""示例：使用重排器。"""
import asyncio

from contextloom.core.models import SearchResult
from contextloom.rerank.bm25 import BM25Reranker


async def main():
    rs = [SearchResult(chunk_id="a", document_id="d", text="苹果", score=0.5),
          SearchResult(chunk_id="b", document_id="d", text="香蕉", score=0.9)]
    out = await BM25Reranker().rerank("苹果", rs)
    print([r.chunk_id for r in out])


if __name__ == "__main__":
    asyncio.run(main())
