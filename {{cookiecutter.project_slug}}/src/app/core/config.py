from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    # FastAPI
    VERSION: str = "0.1.0"
    PROJECT_NAME: str = "EXAMPLE PROJECT"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 1
    API_PREFIX: str = "/api"
    DEBUG: bool = True

    # logger
    LOG_NAME: str = "log.test.record"
    LOG_PATH: str = "./log"
    LOG_FILE_LEVEL: str = "INFO"
    LOG_STREAM_LEVEL: str = "DEBUG"
    LOG_FILE_ENCODING: str = "utf-8"
    LOG_CONSOLE_OUTPUT: bool = True
    LOG_CONSOLE_COLOR: dict = {
        "DEBUG": "white",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    }

    # service
    GPT_PROMPT_TEMPLATE_PATH: str = ""
    GPT_BASE_URL: str = ""
    GPT_API_KEY: str = ""
    GPT_MODEL: str = ""
    GPT_TEMPERATURE: float = 0.8
    GPT_RESPONSE_FORMAT: dict = {"type": "json_object"}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
