from functools import partial

import uvicorn
from fastapi import FastAPI

from app.api.api import router as api_router
from app.core.config import Setting
from app.core.errors import add_exception_handler
from app.core.events import add_middleware, lifespan
from app.core.logging import get_logger

setting = Setting(_env_file=".env", _env_file_encoding="utf-8")
logger = get_logger(setting=setting)
app = FastAPI(
    title=setting.PROJECT_NAME,
    debug=setting.DEBUG,
    version=setting.VERSION,
    lifespan=partial(lifespan, setting=setting, logger=logger),
)
app.include_router(api_router, prefix=setting.API_PREFIX)
add_middleware(app=app, setting=setting)
add_exception_handler(app=app)


def run() -> None:
    uvicorn.run(app, host=setting.HOST, port=setting.PORT, workers=setting.WORKERS)


if __name__ == "__main__":
    run()
