"""写入演示数据到默认知识库。"""
import asyncio

from contextloom.config.settings import Settings
from contextloom.services.document_service import DocumentService


async def main():
    s = Settings(llm_backend="mock", vector_backend="memory",
                 embed_allow_hash_fallback=True, _env_file=None)
    r = await DocumentService(s).ingest("docs/demo/售后手册.md", "default")
    print(r)


if __name__ == "__main__":
    asyncio.run(main())
