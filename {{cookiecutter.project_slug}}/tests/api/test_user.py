import pytest
from fastapi.testclient import TestClient
from {{cookiecutter.project_slug}}.common.config import settings

from tests.conftest import DataStore


@pytest.mark.run(order=1)
def test_user_login_api(client: TestClient, data_store: DataStore):
    url = f"{settings.API_PREFIX}/user/access-token"
    login_data = {
        "username": settings.DEFAULT_SUPERUSER,
        "password": settings.DEFAULT_SUPERUSER_PASSWD,
    }

    response = client.post(url=url, data=login_data)
    tokens = response.json()

    assert response.status_code == 200
    assert response.json()["status"] == 200
    assert "access_token" in tokens
    assert tokens["access_token"]

    # store token data
    data_store.admin_token_data = tokens["access_token"]
    data_store.admin_user_id = tokens["user_id"]
