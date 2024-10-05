from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, EmailStr


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


class UserBase(BaseModel):
    id: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    scopes: Optional[str] = None
    is_active: bool = False
    is_superuser: bool = False
    create_date: Optional[datetime] = None
    profile: Optional[str] = None

    model_config = {"from_attributes": True, "frozen": False}


class UserBaseCreate(UserBase):
    email: EmailStr
    password: str


class UserBaseUpdate(UserBase):
    full_name: str
    password: str
