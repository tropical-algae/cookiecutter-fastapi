from fastapi import APIRouter

from app.api.routes import eventgpt

router = APIRouter()
router.include_router(eventgpt.router, prefix="/v1/eventgpt", tags=["example"])
