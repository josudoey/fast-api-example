import sys
import os
import pytest

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


@pytest.mark.parametrize(
    "item_id, q, expected_status, expected_response",
    [
        (5, "somequery", 200, {"item_id": 5, "q": "somequery"}),  # Happy Path with q
        (5, None, 200, {"item_id": 5, "q": None}),  # Happy Path without q
        ("abc", None, 422, None),  # Bad Path with invalid item_id
    ],
)
def test_read_item(item_id, q, expected_status, expected_response):
    url = f"/items/{item_id}"
    if q is not None:
        url += f"?q={q}"
    response = client.get(url)
    assert response.status_code == expected_status
    if expected_response is not None:
        assert response.json() == expected_response


@pytest.mark.parametrize(
    "item_id, payload, expected_status, expected_response",
    [
        # Happy Paths
        (
            5,
            {"name": "foo", "price": 10.0, "is_offer": True},
            200,
            {"item_id": 5, "name": "foo", "price": 10.0, "is_offer": True},
        ),
        (
            5,
            {"name": "bar", "price": 20.0},
            200,
            {"item_id": 5, "name": "bar", "price": 20.0, "is_offer": None},
        ),
        # Bad Paths
        (5, {"price": 10.0, "is_offer": True}, 422, None),  # Missing name
        (5, {"name": "foo", "is_offer": True}, 422, None),  # Missing price
        (
            5,
            {"name": "foo", "price": "ten", "is_offer": True},
            422,
            None,
        ),  # Invalid price type
    ],
)
def test_update_item(item_id, payload, expected_status, expected_response):
    response = client.put(f"/items/{item_id}", json=payload)
    assert response.status_code == expected_status
    if expected_response is not None:
        assert response.json() == expected_response
