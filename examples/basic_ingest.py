"""示例：摄入文档并提问。"""
import asyncio

from contextloom.config.settings import Settings
from contextloom.services.document_service import DocumentService
from contextloom.services.query_service import QueryService


async def main():
    s = Settings(llm_backend="mock", vector_backend="memory",
                 embed_allow_hash_fallback=True, _env_file=None)
    await DocumentService(s).ingest("docs/demo/售后手册.md", "support")
    answer = await QueryService(s).ask("用第三方耗材还保修吗", "support")
    print(answer.answer)


if __name__ == "__main__":
    asyncio.run(main())
