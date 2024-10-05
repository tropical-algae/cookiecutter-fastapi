import json
import uuid
from typing import Any, Optional, Union

from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}}.app.core.security import get_password_hash, verify_password
from {{cookiecutter.project_slug}}.app.db import schemas
from {{cookiecutter.project_slug}}.app.db.crud.base import CRUDBase
from {{cookiecutter.project_slug}}.app.models.model_user import UserBaseCreate, UserBaseUpdate


class CRUDUser(CRUDBase[schemas.User, UserBaseCreate, UserBaseUpdate]):
    def get_by_full_name(self, db: Session, *, full_name: Optional[str]) -> Optional[schemas.User]:
        db_user = db.query(self.model).filter(self.model.full_name == full_name).first()
        return db_user

    def get_by_id(self, db: Session, *, id: Optional[str]) -> Optional[schemas.User]:
        db_user = db.query(self.model).filter(self.model.id == id).first()
        return db_user

    def create(self, db: Session, *, obj_in: UserBaseCreate) -> schemas.User:
        db_obj = schemas.User(  # type: ignore
            id=obj_in.id if obj_in.id is not None else uuid.uuid4().hex,
            email=obj_in.email,
            password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
            scopes=json.dumps(["USER"]),
            profile=obj_in.profile,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: schemas.User, obj_in: Union[UserBaseUpdate, dict[str, Any]]
    ) -> schemas.User:
        if isinstance(obj_in, dict):
            update_data = obj_in  # pragma: no cover
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, full_name: str, password: str) -> Optional[schemas.User]:
        user = self.get_by_full_name(db, full_name=full_name)
        if not user:
            return None
        if not verify_password(password, str(user.password)):
            return None
        return user


user = CRUDUser(schemas.User)
