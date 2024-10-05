from sqlalchemy import TIMESTAMP, Boolean, Column, String, text

from {{cookiecutter.project_slug}}.app.db.schemas.base import Base
from {{cookiecutter.project_slug}}.app.models.model_user import UserBase


class User(Base[UserBase]):
    # __tablename__ = "user"

    id = Column(String(32), primary_key=True, index=True)
    full_name = Column(String(32), index=True)
    email = Column(String(64), unique=True, index=True, nullable=False)
    password = Column(String(128), nullable=False)
    scopes = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    create_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    profile = Column(String(128), nullable=True)

    def trans(self) -> UserBase:
        return UserBase.model_validate(self)
