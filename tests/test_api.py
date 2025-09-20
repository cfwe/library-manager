
from fastapi.testclient import TestClient


def test_read_root(client: TestClient):
    """ルートエンドポイントのテスト"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Book Management API"}


def test_create_book(client: TestClient):
    """書籍作成エンドポイントのテスト"""
    response = client.post(
        "/api/books/",
        json={"isbn": "9784297100339", "title": "テスト駆動開発"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "テスト駆動開発"
    assert data["isbn"] == "9784297100339"
    assert "id" in data
    assert "created_at" in data
