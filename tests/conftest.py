import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app, get_db
from app.database import Base
from app import models  # Bookモデルをメタデータに登録するためにインポート

# テスト用のインメモリSQLiteデータベースを使用
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """テスト中に `get_db` の依存関係をオーバーライドする関数"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# アプリケーションの依存関係をテスト用のDBセッションに上書き
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    """各テスト関数で独立したDBとAPIクライアントを提供するフィクスチャ"""
    # テストの前にテーブルをすべて作成
    Base.metadata.create_all(bind=engine)
    
    with TestClient(app) as c:
        yield c
        
    # テストの後、テーブルをすべて削除してクリーンな状態に戻す
    Base.metadata.drop_all(bind=engine)
