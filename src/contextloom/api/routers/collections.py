"""知识库管理路由。"""

from __future__ import annotations

from fastapi import APIRouter, Depends

from contextloom.api.deps import get_settings
from contextloom.api.schemas import CollectionCreate
from contextloom.config.settings import Settings

router = APIRouter(prefix="/collections", tags=["collections"])


@router.post("")
async def create_collection(body: CollectionCreate,
                            settings: Settings = Depends(get_settings)) -> dict:
    (settings.collections_dir / body.name).mkdir(parents=True, exist_ok=True)
    return {"name": body.name, "description": body.description, "created": True}


@router.get("")
async def list_collections(settings: Settings = Depends(get_settings)) -> dict:
    dirs = [d.name for d in settings.collections_dir.iterdir() if d.is_dir()]
    return {"collections": sorted(dirs)}
