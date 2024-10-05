from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.project_slug}}.common.config import settings

local_engine = create_engine(url=settings.SQL_DATABASE_URI, pool_pre_ping=True, echo=settings.DEBUG)
LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=local_engine,
)
