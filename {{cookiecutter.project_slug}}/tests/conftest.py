from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from src import app


@pytest.fixture(scope="session", name="client")
def test_client() -> Generator:
    with TestClient(app=app) as tc:
        yield tc
