from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup_success():
    response = client.post("/signup", json={
        "email": "test@example.com",
        "password": "securepassword",
        "full_name": "Test User"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"