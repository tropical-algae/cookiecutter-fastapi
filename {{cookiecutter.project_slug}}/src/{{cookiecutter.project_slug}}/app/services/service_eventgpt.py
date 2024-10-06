from {{cookiecutter.project_slug}}.app.db import schemas
from {{cookiecutter.project_slug}}.app.models.model_eventgpt import EventExtraRequest
from {{cookiecutter.project_slug}}.common.config import settings
from {{cookiecutter.project_slug}}.common.logging import logger
from {{cookiecutter.project_slug}}.common.util import parse_text_2_json
from {{cookiecutter.project_slug}}.service.llm.openai import EventExtraGPT


async def parse_event_2_dict(model: EventExtraGPT, request: EventExtraRequest, user: schemas.User) -> dict[str, str]:
    request_json: dict = request.model_dump()

    input_json: dict = request_json["event"]
    input_json.update(
        {"event_args_num": len(input_json["event_args"]), "event_args": "、".join(input_json["event_args"])}
    )

    logger.info(f"User: {user.full_name}[{user.id}]")

    output = await model.run(
        input=input_json,
        model=request_json["model"],
        temperature=settings.GPT_TEMPERATURE,
        response_format=settings.GPT_RESPONSE_FORMAT,
    )
    output_json, _ = parse_text_2_json(output)
    return output_json
