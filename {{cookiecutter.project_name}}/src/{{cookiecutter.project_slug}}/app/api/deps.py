from collections.abc import AsyncGenerator, Awaitable, Callable

from fastapi import Body, Depends, Header, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from sqlmodel.ext.asyncio.session import AsyncSession

from {{cookiecutter.project_slug}}.app.services.session_service import create_session
from {{cookiecutter.project_slug}}.app.utils.constant import CONSTANT
from {{cookiecutter.project_slug}}.app.utils.security import verift_access_token
from {{cookiecutter.project_slug}}.common.config import settings
from {{cookiecutter.project_slug}}.common.logging import logger
from {{cookiecutter.project_slug}}.core.db.crud import select_user_by_full_name
from {{cookiecutter.project_slug}}.core.db.crud.session_crud import select_session_by_id_and_user
from {{cookiecutter.project_slug}}.core.db.models import UserAccount
from {{cookiecutter.project_slug}}.core.db.session import LocalSession
from {{cookiecutter.project_slug}}.core.model.message import (
    ChatCompleteRequest,
    ChatRequest,
    ChatSessionCompleteRequest,
    ChatSessionRequest,
)
from {{cookiecutter.project_slug}}.core.model.user import ScopeType

AUTHENTICATE_HEADER = "WWW-Authenticate"


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_PREFIX}/user/access-token",
    scopes={
        ScopeType.ADMIN.value: CONSTANT.ROLE_ADMIN_DESCRIPTION,
        ScopeType.USER.value: CONSTANT.ROLE_USER_DESCRIPTION,
        ScopeType.GUEST.value: CONSTANT.ROLE_GUEST_DESCRIPTION,
    },
    auto_error=False,
)


async def get_db() -> AsyncGenerator:
    db = None
    try:
        db = LocalSession()
        yield db
    finally:
        if db:
            await db.close()


async def verity_session_id(
    db: AsyncSession,
    user: UserAccount,
    session_id: str | None = None,
    auto_create_session: bool = True,
) -> ChatSessionCompleteRequest:
    if not session_id:
        if not auto_create_session:
            logger.error(
                "The API is missing session_id and doesn't support automatic creation"
            )
            raise HTTPException(**CONSTANT.RESP_USER_SESSION_NULL)
        session_id = await create_session(db=db, user=user)
        return ChatSessionCompleteRequest(
            user=user,
            session_id=session_id,
            is_new_session=True,
        )

    # When header is not None, select the session status
    result = await select_session_by_id_and_user(db=db, id=session_id, user_id=user.id)
    if result is None:
        logger.error(f"User {user.id} doesn's have session {session_id}")
        raise HTTPException(**CONSTANT.RESP_USER_SESSION_NOT_EXISTS)
    return ChatSessionCompleteRequest(
        user=user,
        session_id=session_id,
        is_new_session=False,
    )


async def get_current_user(
    security_scopes: SecurityScopes,
    db: AsyncSession = Depends(get_db),
    token: str = Depends(reusable_oauth2),
) -> UserAccount:
    headers = {AUTHENTICATE_HEADER: "Bearer"}
    if security_scopes.scopes:
        headers = {AUTHENTICATE_HEADER: f'Bearer scope="{security_scopes.scope_str}"'}
    payload = verift_access_token(token=token, headers=headers)
    user = await select_user_by_full_name(db, full_name=payload.username)
    if user is None:
        raise HTTPException(headers=headers, **CONSTANT.RESP_USER_NOT_EXISTS)
    # Check whether the permission of the current user is in the allowed permission list
    if len(security_scopes.scopes) != 0 and not payload.match_scope(
        security_scopes.scopes
    ):
        raise HTTPException(headers=headers, **CONSTANT.RESP_USER_FORBIDDEN)
    return user


def get_agent_query(
    scopes: list[str] | None = None,
) -> Callable[..., Awaitable[ChatCompleteRequest]]:
    async def _get_agent_query(
        data: ChatRequest = Body(...),
        user: UserAccount = Security(get_current_user, scopes=scopes),
        db: AsyncSession = Depends(get_db),
    ) -> ChatCompleteRequest:
        if not data.use_memory:
            logger.debug("Successfully verified user query (need not memory)")
            return ChatCompleteRequest(
                **data.model_dump(),
                user=user,
                is_new_session=True,
            )

        session_info = await verity_session_id(
            db=db, user=user, session_id=data.session_id, auto_create_session=True
        )
        result = data.model_dump()
        result.update(**session_info.model_dump())
        logger.debug(
            f"Successfully verified user query ({session_info.session_id} is_new: {session_info.is_new_session})"
        )
        return ChatCompleteRequest(**result)

    return _get_agent_query


def get_session_id(
    scopes: list[str] | None = None,
) -> Callable[..., Awaitable[ChatSessionCompleteRequest]]:
    async def _get_session_id(
        data: ChatSessionRequest = Body(...),
        user: UserAccount = Security(get_current_user, scopes=scopes),
        db: AsyncSession = Depends(get_db),
    ) -> ChatSessionCompleteRequest:
        return await verity_session_id(
            db=db, user=user, session_id=data.session_id, auto_create_session=False
        )

    return _get_session_id
