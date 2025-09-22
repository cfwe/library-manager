import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app, get_db
from app.database import Base

# テスト用のSQLiteデータベース設定
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def anyio_backend():
    """anyioのバックエンドとしてasyncioを指定するフィクスチャ"""
    return 'asyncio'


@pytest.fixture(scope="function")
def db_session():
    """
    各テストの前にテーブルをすべて作成し、テスト終了後にすべて削除するフィクスチャ
    """
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """
    テスト用のAPIクライアントを返すフィクスチャ
    """
    def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)