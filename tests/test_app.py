import json
from typing import Any, Generator
from flask.testing import FlaskClient
import pytest

from ..app import app


@pytest.fixture(name="client")
def client_fixture() -> Generator[FlaskClient, Any, None]:
    with app.test_client() as client:
        yield client


def test_success_app(client):
    input_data = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": [],
    }
    response = client.post(
        "/format_hours", data=json.dumps(input_data), content_type="application/json"
    )
    assert response.status_code == 200
    expected_output = (
        "Monday: Closed\n"
        "Tuesday: Closed\n"
        "Wednesday: Closed\n"
        "Thursday: Closed\n"
        "Friday: Closed\n"
        "Saturday: Closed\n"
        "Sunday: Closed"
    )
    assert response.json["readable_hours"] == expected_output


def test_error_app(client):
    input_data = {
        "friday": [{"type": "open", "value": 64800}],  # 6 PM
        "saturday": [
            {"type": "close", "value": 3600},  # 1 AM
            {"type": "open", "value": 32400},  # 9 AM
            {"type": "close", "value": 39600},  # 11 AM
            {"type": "open", "value": 57600},  # 4 PM
            {"type": "close", "value": 82800},  # 11 PM
        ],
    }

    response = client.post(
        "/format_hours", data=json.dumps(input_data), content_type="application/json"
    )

    assert response.status_code == 400

    input_data_1 = {}

    response = client.post(
        "/format_hours", data=json.dumps(input_data_1), content_type="application/json"
    )
