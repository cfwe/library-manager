#!/bin/bash

# 既存のAlembic設定をクリーンアップ
echo "Cleaning up existing Alembic files..."
rm -f alembic.ini
rm -rf alembic

# Alembic環境を初期化
echo "Initializing Alembic environment..."
docker compose run --rm backend alembic init alembic

# alembic.ini のデータベース接続URLを環境変数から読み込むように修正
echo "Configuring alembic.ini..."
FILE="alembic.ini"
sed -i 's|^sqlalchemy\.url *=.*$|sqlalchemy.url = \${DATABASE_URL}|' "$FILE"
# prepend_sys_path = . の行をコメントアウト
sed -i 's|^prepend_sys_path *= *\.|# prepend_sys_path = .|' "$FILE"

echo "Alembic initialization complete."

# databaseのマイグレーション
# docker compose run --rm backend alembic revision --autogenerate -m "Create initial tables"

# booksテーブルの作成
# docker compose run --rm backend alembic upgrade head
