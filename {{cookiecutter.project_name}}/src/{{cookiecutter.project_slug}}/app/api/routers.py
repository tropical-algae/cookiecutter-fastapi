from fastapi import APIRouter

from {{cookiecutter.project_slug}}.app.api.endpoints import chat, health, session, tool, user

router = APIRouter()
router.include_router(health.router, prefix="/system", tags=["system status"])
router.include_router(user.router, prefix="/user", tags=["user"])
router.include_router(tool.router, prefix="/tool", tags=["agent tool"])
router.include_router(chat.router, prefix="/model", tags=["chat with agent/llm"])
router.include_router(session.router, prefix="/session", tags=["chat session"])
