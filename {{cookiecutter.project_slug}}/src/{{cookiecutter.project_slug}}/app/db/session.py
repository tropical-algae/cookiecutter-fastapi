from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel, create_engine

from {{cookiecutter.project_slug}}.app.db.models import *
from {{cookiecutter.project_slug}}.common.config import settings

local_engine = create_engine(
    url=settings.SQL_DATABASE_URI, pool_pre_ping=True, echo=settings.DEBUG
)
LocalSession = sessionmaker(
    autocommit=False, autoflush=False, bind=local_engine, class_=Session
)

SQLModel.metadata.create_all(local_engine)
