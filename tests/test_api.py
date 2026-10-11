import pytest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "active"

def test_auth_nonexistent_user():
    response = client.post("/auth/nonexistentuser999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
