import pytest
from fastapi.testclient import TestClient

from {{cookiecutter.project_slug}}.common.config import settings
from {{cookiecutter.project_slug}}.core.model.base import SystemStatusType
from {{cookiecutter.project_slug}}.core.model.user import ScopeType
from tests.conftest import DataStore

FAKE_SESION_ID: str = "FAKEID"


@pytest.mark.run(order=5)
def test_session_check_api(client: TestClient, data_store: DataStore):
    header = {"Authorization": f"Bearer {data_store.admin_token_data}"}
    url = f"{settings.API_PREFIX}/session/list"
    response = client.get(url=url, headers=header)
    assert response.status_code == 200


@pytest.mark.run(order=6)
def test_model_check_api(client: TestClient):
    url = f"{settings.API_PREFIX}/model/list"
    response = client.get(url=url)
    assert response.status_code == 200


@pytest.mark.run(order=6)
def test_tool_check_api(client: TestClient):
    url = f"{settings.API_PREFIX}/tool/list"
    response = client.get(url=url)
    assert response.status_code == 200


@pytest.mark.run(order=7)
@pytest.mark.parametrize(
    "session_id",
    [FAKE_SESION_ID],
)
def test_message_check_api(client: TestClient, data_store: DataStore, session_id: str):
    header = {
        "Authorization": f"Bearer {data_store.admin_token_data}",
    }
    data = {"session_id": session_id}
    url = f"{settings.API_PREFIX}/session/messages"
    response = client.post(url=url, headers=header, json=data)
    assert response.status_code == 404
