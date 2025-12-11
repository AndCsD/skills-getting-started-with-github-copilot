import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_unregister():
    # Signup
    response = client.post("/activities/Chess Club/signup?email=testuser@mergington.edu")
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    # Unregister
    response = client.request(
        "DELETE",
        "/activities/Chess Club/unregister",
        json={"email": "testuser@mergington.edu"}
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
