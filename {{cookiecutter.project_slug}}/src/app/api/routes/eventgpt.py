from logging import Logger

from fastapi import APIRouter, HTTPException, Request

from app.models.eventgpt import (
    EventExtraRequest,
    EventExtraResponse,
)
from app.services.eventgpt import parse_event_2_dict
from service.openapi_model import EventExtraGPT

router = APIRouter()


@router.post("/complete", response_model=EventExtraResponse)
async def predict(request: Request, data_input: EventExtraRequest):
    logger: Logger = request.app.state.logger
    model: EventExtraGPT = request.app.state.eventgpt
    try:
        output = parse_event_2_dict(model=model, input=data_input)
        if output is None:
            raise HTTPException(status_code=500, detail="Exception: Can not ")
    except Exception as err:
        logger.info(f"Event extraction model inference error! {err}")
        raise HTTPException(status_code=500, detail=f"Exception: {err}") from err

    return EventExtraResponse(data=output)
