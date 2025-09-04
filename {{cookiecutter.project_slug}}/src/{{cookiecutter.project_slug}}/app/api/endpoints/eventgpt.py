from typing import Any

from fastapi import APIRouter, HTTPException, Request, Security

from {{cookiecutter.project_slug}}.app.api.deps import get_current_user
from {{cookiecutter.project_slug}}.app.db.models import User
from {{cookiecutter.project_slug}}.app.services.eventgpt import parse_event_2_dict
from {{cookiecutter.project_slug}}.common.logging import logger
from {{cookiecutter.project_slug}}.common.model.eventgpt import (
    EventExtraRequest,
    EventExtraResponse,
)
from {{cookiecutter.project_slug}}.core.llm.eventgpt import EventExtraGPT, event_extra

router = APIRouter()


@router.post("/complete", response_model=EventExtraResponse)
async def predict(
    data_input: EventExtraRequest,
    current_user: User = Security(get_current_user, scopes=["ADMIN", "USER"]),
) -> Any:
    try:
        output = await parse_event_2_dict(
            model=event_extra, request=data_input, user=current_user
        )
        if output is None:
            raise HTTPException(
                status_code=500,
                detail="ERROR: Cannot process model output into standardized format.",
            )
    except Exception as err:
        logger.info(f"Event extraction model inference error! {err}")
        raise HTTPException(status_code=500, detail=f"ERROR: {err}") from err

    return EventExtraResponse(data=output)
