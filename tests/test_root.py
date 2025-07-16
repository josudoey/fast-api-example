import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    response = client.get("/items/5?q=somequery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "somequery"}


def test_update_item():
    response = client.put(
        "/items/5",
        json={"name": "foo", "price": 10.0, "is_offer": True},
    )
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 5,
        "name": "foo",
        "price": 10.0,
        "is_offer": True,
    }
