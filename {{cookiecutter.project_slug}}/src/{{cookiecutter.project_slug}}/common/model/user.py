import json
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, EmailStr, Field

from {{cookiecutter.project_slug}}.app.db.models import User


class Token(BaseModel):
    user_id: str
    access_token: str
    token_type: str
    message: str
    timestamp: datetime
    scopes: list[str]
    status: int


class TokenData(BaseModel):
    id: str
    username: Union[str, None] = None
    scopes: list[str] = []


class UserBasicInfo(BaseModel):
    full_name: str = Field(description="User name")
    password: str = Field(description="User password")
    email: str = Field(default="admin@test.com", description="The email of user")
    scopes: list = Field(
        default_factory=list, description="The scope for user, include ADMIN, USER, GUEST"
    )

    def build_user(self) -> User:
        return User(
            full_name=self.full_name,
            password=self.password,
            email=self.email,
            scopes=json.dumps(self.scopes),
            is_superuser=False,
            is_active=True,
        )
