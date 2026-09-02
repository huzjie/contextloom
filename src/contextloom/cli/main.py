"""命令行入口。"""

from __future__ import annotations

import asyncio

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from contextloom import __version__
from contextloom.config.settings import load_settings
from contextloom.logging import setup_logging

app = typer.Typer(name="contextloom", help="ContextLoom - 端侧百万上下文文档智能平台",
                  no_args_is_help=True)
console = Console()


def _settings():
    s = load_settings()
    setup_logging(s.log_level)
    return s


@app.command()
def version() -> None:
    console.print(f"ContextLoom v{__version__}")


@app.command()
def ingest(source: str = typer.Argument(..., help="文件/目录/URL"),
           collection: str = typer.Option("default", "--collection", "-c")) -> None:
    from contextloom.services.document_service import DocumentService
    settings = _settings()
    result = asyncio.run(DocumentService(settings).ingest(source, collection))
    console.print(f"✅ 已摄入 [bold]{result['title']}[/bold] "
                  f"→ {result['chunks']} 个分块（知识库：{collection}）")


@app.command()
def ask(question: str = typer.Argument(..., help="问题"),
        collection: str = typer.Option("default", "--collection", "-c")) -> None:
    from contextloom.services.query_service import QueryService
    settings = _settings()
    answer = asyncio.run(QueryService(settings).ask(question, collection))
    console.print(Markdown(answer.answer))
    console.print(f"\n[dim]后端 {answer.backend} / {answer.model} · "
                  f"{answer.elapsed_ms}ms · {len(answer.sources)} 来源[/dim]")


@app.command()
def search(query: str = typer.Argument(...),
           collection: str = typer.Option("default", "--collection", "-c")) -> None:
    from contextloom.services.query_service import QueryService
    settings = _settings()
    results = asyncio.run(QueryService(settings).search(query, collection))
    table = Table(title=f"检索结果（{len(results)}）")
    table.add_column("分数", justify="right")
    table.add_column("片段", max_width=80)
    for r in results:
        table.add_row(f"{r.score:.3f}", r.text[:120].replace("\n", " "))
    console.print(table)


@app.command()
def serve(host: str = typer.Option(None, "--host"), port: int = typer.Option(None, "--port"),
          reload: bool = typer.Option(False, "--reload")) -> None:
    import uvicorn
    settings = _settings()
    console.print(f"🚀 启动 ContextLoom：http://{host or settings.host}:{port or settings.port}")
    uvicorn.run("contextloom.api.app:app", host=host or settings.host,
                port=port or settings.port, reload=reload)


@app.command()
def doctor() -> None:
    settings = _settings()
    from contextloom.llm.factory import create_backend
    from contextloom.vectorstore.factory import create_store
    table = Table(title="ContextLoom 环境自检")
    table.add_column("检查项")
    table.add_column("状态")
    table.add_column("详情")
    store = create_store(settings)
    table.add_row("向量后端", "✅", f"{store.name} @ {settings.index_dir}")
    backend = create_backend(settings)
    table.add_row("LLM 后端", "✅", f"{backend.name} / {settings.llm_model} @ {settings.llm_base_url}")
    table.add_row("上下文窗口", "✅", f"{settings.llm_context_window} tokens")
    console.print(table)


if __name__ == "__main__":
    app()
