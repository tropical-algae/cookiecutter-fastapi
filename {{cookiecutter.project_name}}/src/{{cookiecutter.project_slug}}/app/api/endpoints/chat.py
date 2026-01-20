from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from {{cookiecutter.project_slug}}.app.api.deps import get_agent_query, get_session_id
from {{cookiecutter.project_slug}}.app.services.inference_service import agent_response, agent_stream_response
from {{cookiecutter.project_slug}}.common.config import settings
from {{cookiecutter.project_slug}}.core.model.message import AgentResponse, ChatCompleteRequest
from {{cookiecutter.project_slug}}.core.model.user import ScopeType

router = APIRouter()


@router.get("/list")
async def get_agent_models() -> list[str]:
    return settings.AGENT_OPTIONAL_MODELS


@router.post("/chat", response_model=AgentResponse, response_model_exclude={"tools_call"})
async def agent_chat(
    chat_request: ChatCompleteRequest = Depends(
        get_agent_query(scopes=[ScopeType.ADMIN, ScopeType.USER])
    ),
):
    return await agent_response(chat_request=chat_request)


@router.post("/chat/stream")
async def agent_chat_stream(
    chat_request: ChatCompleteRequest = Depends(
        get_agent_query(scopes=[ScopeType.ADMIN, ScopeType.USER])
    ),
):
    return StreamingResponse(agent_stream_response(chat_request=chat_request))
