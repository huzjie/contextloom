"""检索/生成延迟基准测试。"""
import argparse
import asyncio
import time

from contextloom.config.settings import Settings
from contextloom.services.query_service import QueryService


async def run(collection: str, questions: list[str], settings: Settings):
    svc = QueryService(settings)
    for q in questions:
        t0 = time.perf_counter()
        a = await svc.ask(q, collection)
        dt = (time.perf_counter() - t0) * 1000
        print(f"[{dt:7.1f}ms] {q} -> {a.answer[:50]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--collection", default="default")
    ap.add_argument("--questions", nargs="+", default=["问题一", "问题二"])
    args = ap.parse_args()
    s = Settings(llm_backend="mock", vector_backend="memory",
                 embed_allow_hash_fallback=True, _env_file=None)
    asyncio.run(run(args.collection, args.questions, s))


if __name__ == "__main__":
    main()
