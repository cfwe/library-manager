# タスク分解 - 蔵書管理アプリ

## フェーズ1: Backend APIの基本構築

- [x] 開発環境のセットアップ (Docker, FastAPI, Uvicorn)
- [x] `doc/design.md` に基づくディレクトリ構成の作成
- [x] データベース接続設定 (`database.py`)
- [x] SQLAlchemyモデルの定義 (`models.py`)
- [x] Pydanticスキーマの定義 (`schemas.py`)
- [x] **データベースマイグレーションツールの導入 (Alembic)**
    - [x] Alembicの初期化と設定
    - [x] 最初のマイグレーションファイルを作成 (`Create books table`)
    - [x] マイグレーションをデータベースに適用
- [x] 書籍のCRUD操作関数の実装 (`crud.py`)
- [x] 書籍CRUDのAPIエンドポイント実装 (`main.py`)
    - [x] `POST /api/books/`
    - [x] `GET /api/books/`
    - [x] `GET /api/books/{book_id}`
    - [x] `PUT /api/books/{book_id}`
    - [x] `DELETE /api/books/{book_id}`
- [x] ここまでのAPI動作をSwagger UIで手動テスト

## フェーズ2: 外部API連携機能の実装

- [x] ISBNから書籍情報を取得するサービスの開発 (`services/book_lookup.py`)
    - [x] openBDなどのAPI選定と仕様調査
    - [x] APIクライアントの実装
- [x] 書籍情報取得エンドポイントの実装 (`GET /api/lookup_book/{isbn}`)
- [ ] 中古価格を調査するサービスの開発
    - [ ] スクレイピングまたはAPIの調査・選定
    - [ ] 価格取得ロジックの実装
- [ ] 中古価格調査エンドポイントの実装 (`GET /api/books/{book_id}/market_price`)

## フェーズ3: Frontendの基本構築

- [ ] Frontend開発環境のセットアップ (Node.js, Vite, React/Vueなど)
- [ ] 蔵書一覧ページの作成
- [ ] 書籍登録ページの作成

## フェーズ4: テストと改善

- [x] Backendの単体テスト・結合テスト作成 (Pytest)
- [ ] UI/UXの改善
