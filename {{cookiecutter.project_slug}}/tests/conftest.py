from collections.abc import Generator
from typing import Optional

import pytest
from fastapi.testclient import TestClient
from {{cookiecutter.project_slug}}.app.db.schemas.schema_user import User
from {{cookiecutter.project_slug}}.main import app
from pydantic import BaseModel


class DataStore(BaseModel):
    admin_token_data: Optional[str] = None
    admin_user_id: Optional[str] = None


@pytest.fixture(scope="session", name="client")
def test_client() -> Generator:
    with TestClient(app=app) as tc:
        yield tc


@pytest.fixture(scope="session", name="data_store")
def test_data_store() -> DataStore:  # type: ignore
    return DataStore()
