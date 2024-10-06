from typing import Any

from fastapi import APIRouter, HTTPException, Request, Security

from {{cookiecutter.project_slug}}.app.api import deps
from {{cookiecutter.project_slug}}.app.db import schemas
from {{cookiecutter.project_slug}}.app.models.model_eventgpt import (
    EventExtraRequest,
    EventExtraResponse,
)
from {{cookiecutter.project_slug}}.app.services.service_eventgpt import parse_event_2_dict
from {{cookiecutter.project_slug}}.common.logging import logger
from {{cookiecutter.project_slug}}.service.llm.openai import EventExtraGPT

router = APIRouter()


@router.post("/complete", response_model=EventExtraResponse)
async def predict(
    data_input: EventExtraRequest,
    request: Request,
    current_user: schemas.User = Security(deps.get_current_user, scopes=["ADMIN", "USER"]),
) -> Any:
    model: EventExtraGPT = request.app.state.eventgpt

    try:
        output = await parse_event_2_dict(model=model, request=data_input, user=current_user)
        if output is None:
            raise HTTPException(
                status_code=500,
                detail="ERROR: Cannot process model output into standardized format.",
            )
    except Exception as err:
        logger.info(f"Event extraction model inference error! {err}")
        raise HTTPException(status_code=500, detail=f"ERROR: {err}") from err

    return EventExtraResponse(data=output)
