# 蔵書管理アプリ

個人が所有する蔵書を効率的にデジタル化し、一元管理することを目的としたWebアプリケーションです。

## 主な機能

- **書籍情報の登録・編集・削除**: ISBNによる自動検索、または手動での入力で蔵書を管理できます。
- **外部API連携**: openBDと国立国会図書館サーチAPIを利用して、ISBNから書籍情報を自動で取得します。
- **中古価格調査**: ブックオフオンラインをスクレイピングし、書籍のおおよその中古市場価格を調査します。

## 技術スタック

- **Backend**: Python, FastAPI
- **Frontend**: Jinja2, Vanilla JavaScript (FastAPIによるサーバーサイドレンダリング)
- **Database**: PostgreSQL
- **Infrastructure**: Docker, Docker Compose
- **DB Migration**: Alembic
- **Testing**: Pytest

## 環境構築と起動方法

### 1. 前提条件

- Docker
- Docker Compose
- (Windowsの場合) WSL2

### 2. リポジトリのクローン

```bash
git clone <リポジトリのURL>
cd <リポジトリのディレクトリ名>
```

### 3. 環境変数の設定

`.env.example` をコピーして `.env` ファイルを作成します。通常、中身を編集する必要はありません。

```bash
cp .env.example .env
```

### 4. Dockerコンテナのビルドと起動

以下のコマンドで、アプリケーションとデータベースのコンテナをビルドし、バックグラウンドで起動します。

```bash
docker compose up --build -d
```

### 5. データベースマイグレーションの実行

初回起動時、またはデータベースのテーブル構造に変更があった場合に、以下のコマンドを実行してテーブルを作成・更新します。

```bash
docker compose run --rm backend alembic upgrade head
```

### 6. アプリケーションへのアクセス

ブラウザで以下のURLにアクセスしてください。

- **Webアプリケーション**: http://localhost:8000
- **APIドキュメント (Swagger UI)**: http://localhost:8000/docs

## テストの実行方法

以下のコマンドで、バックエンドのテストを実行できます。

```bash
docker compose run --rm test
```