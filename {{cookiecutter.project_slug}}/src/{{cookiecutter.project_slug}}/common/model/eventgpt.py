from pydantic import BaseModel


class EventData(BaseModel):
    event_args: list[str] = ["时间", "地点", "事件主体", "事件客体", "事件影响"]
    language: str = "中文"
    data: str = ""


class EventExtraRequest(BaseModel):
    event: EventData
    model: str = "gpt-3.5-turbo-ca"


class EventExtraResponse(BaseModel):
    data: dict
