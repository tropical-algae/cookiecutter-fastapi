from app.models.eventgpt import EventExtraRequest
from service.openapi_model import EventExtraGPT
from utils.util import parse_text_2_json


def parse_event_2_dict(model: EventExtraGPT, input: EventExtraRequest) -> dict[str, str]:
    input_json: dict = input.model_dump()

    input_json["event_args_num"] = len(input_json["event_args"])
    input_json["event_args"] = "、".join(input_json["event_args"])

    output = model.run(input_json)
    output_json, _ = parse_text_2_json(output)
    return output_json
