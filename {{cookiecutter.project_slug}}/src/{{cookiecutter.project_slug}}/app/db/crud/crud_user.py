import json
import uuid
from copy import deepcopy

from sqlmodel import Session, select

from {{cookiecutter.project_slug}}.app.db.models import User
from {{cookiecutter.project_slug}}.app.utils.security import get_password_hash, verify_password


def select_all_user(db: Session) -> list[User]:
    users = db.exec(select(User)).all()
    return list(users)


def get_by_full_name(db: Session, full_name: str | None) -> User | None:
    if full_name:
        user_result = db.exec(select(User).where(User.full_name == full_name)).first()
        return user_result
    return None


def create_user(db: Session, user: User):
    user.password = get_password_hash(user.password)
    user.id = user.id or uuid.uuid4().hex

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, *, user_id: str, update_attr: dict) -> User | None:
    user = db.get(User, ident=user_id)
    if user:
        user.email = update_attr.get("email", user.email)
        user.password = (
            get_password_hash(update_attr["password"])
            if update_attr.get("passwd")
            else user.password
        )
        user.full_name = update_attr.get("full_name", user.full_name)

        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    return None


def authenticate_user(db: Session, *, full_name: str, password: str) -> User | None:
    user = get_by_full_name(db, full_name=full_name)
    if not user:
        return None
    if not verify_password(password, str(user.password)):
        return None
    return user
