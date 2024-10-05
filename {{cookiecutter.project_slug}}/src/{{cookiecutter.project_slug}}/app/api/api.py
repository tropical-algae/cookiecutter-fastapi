from fastapi import APIRouter

from {{cookiecutter.project_slug}}.app.api.routes import eventgpt, user

router = APIRouter()
router.include_router(eventgpt.router, prefix="/eventgpt", tags=["example_event_gpt"])
router.include_router(user.router, prefix="/user", tags=["user"])
