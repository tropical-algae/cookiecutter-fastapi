from pydantic import BaseModel


class EventExtraRequest(BaseModel):
    event_args: list[str] = ["时间", "地点", "事件主体", "事件客体", "事件影响"]
    language: str = "中文"
    data: str = ""


class EventExtraResponse(BaseModel):
    data: dict
