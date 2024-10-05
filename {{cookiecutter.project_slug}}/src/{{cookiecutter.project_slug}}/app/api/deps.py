from collections.abc import Generator

import jose
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}}.app.core.constant import CONSTANT
from {{cookiecutter.project_slug}}.app.db import crud, schemas
from {{cookiecutter.project_slug}}.app.db.session import LocalSession
from {{cookiecutter.project_slug}}.app.models import model_user
from {{cookiecutter.project_slug}}.common.config import settings
from {{cookiecutter.project_slug}}.common.logging import logger

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_PREFIX}/user/access-token",
    scopes={
        "ADMIN": CONSTANT.ROLE_ADMIN_DESCRIPTION,
        "USER": CONSTANT.ROLE_USER_DESCRIPTION,
        "GUEST": CONSTANT.ROLE_GUEST_DESCRIPTION,
    },
    auto_error=False,
)


def get_db() -> Generator:
    db = None
    try:
        db = LocalSession()
        yield db
    finally:
        if db:
            db.close()


async def get_current_user(
    security_scopes: SecurityScopes,
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2),
) -> schemas.User:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=CONSTANT.TOKEN_NOT_MATCH,
        headers={"WWW-Authenticate": authenticate_value},
    )
    if token is None:
        raise credentials_exception
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        username = payload.get("username")
        userid = payload.get("userid")
        if username is None:
            raise credentials_exception  # pragma: no cover
        token_scopes = payload.get("scopes", [])
        token_data = model_user.TokenData(scopes=token_scopes, username=username, id=userid)
    except (jose.exceptions.JWTError, ValidationError) as err:
        logger.error(f"Security verification failed: {err}")
        raise credentials_exception from err
    # get user from db
    user = crud.user.get_by_full_name(db, full_name=token_data.username)
    if user is None:  # pragma: no cover
        raise credentials_exception
    # Check whether the permission of the current user is in the allowed permission list
    if len(security_scopes.scopes) != 0 and not any(sc in security_scopes.scopes for sc in token_data.scopes):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=CONSTANT.USER_NOT_ENOUGH_PERMISSION,
            headers={"WWW-Authenticate": authenticate_value},
        )
    return user
