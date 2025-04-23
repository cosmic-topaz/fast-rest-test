from fastapi.testclient import TestClient
from app.main import app
from app.core.security import get_password_hash
from app.models import User
from app.database import SessionLocal

client = TestClient(app)

def create_test_user():
    db = SessionLocal()
    user = User(
        email="jwtuser@example.com",
        hashed_password=get_password_hash("testpassword"),
        full_name="JWT User"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()

def test_jwt_auth_flow():
    create_test_user()

    # 로그인해서 JWT 발급 받기
    response = client.post("/login", json={
        "email": "jwtuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    token = response.json()["access_token"]
    assert token

    # JWT 토큰을 사용해 /me 요청
    headers = {"Authorization": f"Bearer {token}"}
    me_response = client.get("/me", headers=headers)
    assert me_response.status_code == 200
    assert me_response.json()["email"] == "jwtuser@example.com"

def test_me_authenticated(client):
    # 테스트 유저 생성
    client.post("/signup", json={
        "email": "jwt@example.com",
        "password": "pass123",
        "full_name": "JWT Tester"
    })

    # 로그인 → 토큰 발급
    res = client.post("/login", json={
        "email": "jwt@example.com",
        "password": "pass123"
    })
    token = res.json()["access_token"]

    # 토큰으로 인증 요청
    headers = {"Authorization": f"Bearer {token}"}
    res = client.get("/me", headers=headers)

    assert res.status_code == 200
    assert res.json()["email"] == "jwt@example.com"