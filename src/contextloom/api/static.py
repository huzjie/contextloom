"""挂载静态 Web 控制台。"""

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(tags=["ui"])
_INDEX = Path(__file__).resolve().parent.parent / "webui" / "index.html"


@router.get("/ui")
async def ui() -> FileResponse:
    return FileResponse(_INDEX)
