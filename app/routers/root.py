from fastapi import APIRouter
from app.routers import items

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}


router.include_router(items.router)
