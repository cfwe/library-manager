
from app.main import app, get_db
from app.database import Base
from app import models  # Bookモデルをメタデータに登録するためにインポート

# テスト用のインメモリSQLiteデータベースを使用
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

