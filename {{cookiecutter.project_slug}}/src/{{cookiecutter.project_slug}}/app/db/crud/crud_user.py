import json
import uuid

# from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select

from {{cookiecutter.project_slug}}.app.core.security import get_password_hash, verify_password
from {{cookiecutter.project_slug}}.app.db.models import User


def select_all_user(db: Session) -> list[User]:
    users = db.exec(select(User)).all()
    return list(users)


def get_by_full_name(db: Session, full_name: str | None) -> User | None:
    if full_name:
        user_result = db.exec(select(User).where(User.full_name == full_name)).first()
        return user_result
    return None


def create_user(db: Session, user: User):
    db_obj = User(  # type: ignore
        id=user.id if user.id is not None else uuid.uuid4().hex,
        email=user.email,
        password=get_password_hash(user.password),
        full_name=user.full_name,
        is_superuser=user.is_superuser,
        scopes=json.dumps(["USER"]),
        profile=user.profile,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_user(db: Session, *, user_id: str, update_attr: dict) -> User | None:
    user = db.get(User, ident=user_id)
    if user:
        user.email = update_attr.get("email", user.email)
        user.password = get_password_hash(update_attr["password"]) if update_attr.get("passwd") else user.password
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
