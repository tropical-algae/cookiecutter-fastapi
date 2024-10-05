from {{cookiecutter.project_slug}}.app.db import schemas
from {{cookiecutter.project_slug}}.app.models.model_eventgpt import EventExtraRequest
from {{cookiecutter.project_slug}}.common.logging import logger
from {{cookiecutter.project_slug}}.common.util import parse_text_2_json
from {{cookiecutter.project_slug}}.service.openapi_model import EventExtraGPT


def parse_event_2_dict(model: EventExtraGPT, input: EventExtraRequest, user: schemas.User) -> dict[str, str]:
    input_json: dict = input.model_dump()

    input_json["event_args_num"] = len(input_json["event_args"])
    input_json["event_args"] = "、".join(input_json["event_args"])

    logger.info(f"User: {user.full_name}[{user.id}]")

    output = model.run(input_json)
    output_json, _ = parse_text_2_json(output)
    return output_json
