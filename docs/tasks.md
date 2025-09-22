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
- [x] 中古価格・定価を調査するサービスの開発 (`services/market_price_scraper.py`)
    - [x] Book-Off OnlineのWebサイトを調査
    - [x] スクレイピングによる価格取得ロジックの実装
- [x] 価格調査エンドポイントの実装
    - [x] `GET /api/prices/{isbn}` (DB登録なしでの価格調査)
    - [x] `GET /api/books/{isbn}/update_prices` (登録済み書籍の価格更新)
  
## フェーズ3: Frontendの基本構築

- [x] Frontend開発環境のセットアップ (Node.js, Vite, React)
- [ ] 蔵書一覧ページの作成
- [ ] 書籍登録ページの作成
- [x] Jinja2テンプレートによる基本的なUIの作成 (`templates/index.html`)
- [x] 蔵書一覧ページの作成
- [x] ISBNによる書籍登録機能の実装
- [x] 手動登録・編集モーダルの実装

## フェーズ4: テストと改善

- [x] Backendの単体テスト・結合テスト作成 (Pytest)
- [ ] UI/UXの改善
- [x] UI/UXの改善（キーワード・出版社での絞り込み、全角ISBNの自動変換など）