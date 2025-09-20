# 設計 - 蔵書管理アプリ

## 1. システムアーキテクチャ

- **Frontend** と **Backend** を分離した構成とする。
- Frontendは静的ファイルを配信し、ブラウザ上で動作するSPA（Single Page Application）を想定。
- BackendはFastAPIを使用し、JSON形式でデータをやり取りするRESTful APIサーバーを構築する。
- データ永続化のためにデータベース（PostgreSQL）を使用する。

```
┌──────────┐     HTTP(JSON)     ┌──────────┐     SQL     ┌────────────┐
│ Frontend │<------------------>│ Backend  │<----------->│ Database   │
│ (Browser)│                    │ (FastAPI)│             │ (PostgreSQL) │
└──────────┘                    └────┬─────┘             └────────────┘
                                     │ HTTP(JSON)
                                     │
                               ┌─────▼─────┐
                               │ 外部API   │
                               │(openBD etc)│
                               └───────────┘
```

## 2. データベース設計

- `books` テーブルを1つ作成する。

**books テーブル**
| カラム名 | データ型 | 説明 | 制約 |
|:---|:---|:---|:---|
| id | INTEGER | 主キー | PRIMARY KEY, AUTOINCREMENT |
| isbn | VARCHAR(13) | ISBNコード | UNIQUE, NOT NULL |
| title | VARCHAR(255) | 書籍タイトル | NOT NULL |
| author | VARCHAR(255) | 著者 | |
| publisher | VARCHAR(255) | 出版社 | |
| page_count | INTEGER | ページ数 | |
| size | VARCHAR(50) | 判型 (例: A5, 文庫) | |
| purchase_date | DATE | 購入日 | |
| purchase_price | INTEGER | 購入価格（円） | |
| condition | VARCHAR(50) | 本の状態 | |
| summary | TEXT | 要約・メモ | |
| market_price | INTEGER | 中古価格（円） | |
| created_at | TIMESTAMP | 作成日時 | |
| updated_at | TIMESTAMP | 更新日時 | |

### データベースマイグレーション
- データベースのスキーマ（テーブル構造）の変更は、マイグレーションツール **Alembic** を使用して管理する。
- `app/models.py` の変更を元にマイグレーションファイルを作成し、それを適用することで、安全かつ再現可能な方法でデータベースを更新する。

## 3. Backendディレクトリ構成

```
/
├── alembic/          # Alembicのマイグレーションスクリプト
├── app/              # FastAPIアプリケーションコード
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
├── alembic.ini       # Alembicの設定ファイル
└── docker-compose.yml
```
