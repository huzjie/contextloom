"""示例：纯检索（不经过 LLM）。"""
import asyncio

from contextloom.config.settings import Settings
from contextloom.services.query_service import QueryService


async def main():
    s = Settings(llm_backend="mock", vector_backend="memory",
                 embed_allow_hash_fallback=True, _env_file=None)
    results = await QueryService(s).search("关键词", "default", top_k=5)
    for r in results:
        print(f"[{r.score:.3f}] {r.text[:60]}")


if __name__ == "__main__":
    asyncio.run(main())
