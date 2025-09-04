from datetime import datetime
from typing import Optional

from sqlalchemy import BOOLEAN, TIMESTAMP, Column, Index, String, text
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __table_args__ = (
        Index("ix_user_email", "email", unique=True),
        Index("ix_user_full_name", "full_name"),
        Index("ix_user_id", "id"),
    )

    id: Optional[str] = Field(
        default=None, sa_column=Column("id", String(32), primary_key=True)
    )
    email: str = Field(sa_column=Column("email", String(64), nullable=False))
    password: str = Field(sa_column=Column("password", String(128), nullable=False))
    scopes: str = Field(sa_column=Column("scopes", String(128), nullable=False))
    full_name: Optional[str] = Field(
        default=None, sa_column=Column("full_name", String(32))
    )
    is_active: Optional[bool] = Field(
        default=None, sa_column=Column("is_active", BOOLEAN)
    )
    is_superuser: Optional[bool] = Field(
        default=None, sa_column=Column("is_superuser", BOOLEAN)
    )
    create_date: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            "create_date", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
        ),
    )
    profile: Optional[str] = Field(default=None, sa_column=Column("profile", String(128)))
