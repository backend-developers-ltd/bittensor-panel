from unittest.mock import MagicMock

import pytest
from django.contrib.messages import get_messages
from django.test import Client
from pytest_mock import MockerFixture

from bittensor_panel.core.services import HyperParameterRefreshFailed


@pytest.fixture
def mock_refresh_hyperparams(mocker: MockerFixture):
    return mocker.patch("bittensor_panel.core.admin.refresh_hyperparams")


def test_refresh_hyperparams_view(
    admin_client: Client, mock_refresh_hyperparams: MagicMock
):
    response = admin_client.post("/admin/core/hyperparameter/refresh-hyperparams/")

    mock_refresh_hyperparams.assert_called_once()

    assert response.status_code == 302
    assert response.url == "/admin/core/hyperparameter/"


def test_refresh_hyperparams_view_exception(
    admin_client: Client, mock_refresh_hyperparams: MagicMock
):
    mock_refresh_hyperparams.side_effect = HyperParameterRefreshFailed("error")

    response = admin_client.post("/admin/core/hyperparameter/refresh-hyperparams/")

    assert response.status_code == 302
    assert response.url == "/admin/core/hyperparameter/"

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
