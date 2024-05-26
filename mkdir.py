# osモジュールを使用してディレクトリ構造を作成し、def.mdファイルを生成するPythonコード

import os

def create_directory_structure():
    # ディレクトリ構造を定義
    directories = [
        "src/frontend/components",
        "src/frontend/pages",
        "src/frontend/styles",
        "src/backend/api",
        "src/backend/models",
        "src/backend/services",
        "tests/unit",
        "tests/integration",
        "docs/api",
        "docs/user",
        "config",
        "build/scripts"
    ]
    
    # 各ディレクトリを作成
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # ファイルを作成
    files = {
        "config/dev.env": "",
        "config/prod.env": "",
        "build/Dockerfile": ""
    }
    
    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

def generate_def_md():
    content = """
|-- src                : ソースコードを格納するディレクトリ
|   |-- frontend       : フロントエンドのソースコードを格納するディレクトリ
|       |-- components : フロントエンドのコンポーネントを格納するディレクトリ
|       |-- pages      : 各ページのソースコードを格納するディレクトリ
|       `-- styles     : スタイルシートを格納するディレクトリ
|   `-- backend        : バックエンドのソースコードを格納するディレクトリ
|       |-- api        : APIエンドポイントのソースコードを格納するディレクトリ
|       |-- models     : データベースモデルを格納するディレクトリ
|       `-- services   : ビジネスロジックを格納するディレクトリ
|-- tests              : テストコードを格納するディレクトリ
|   |-- unit           : 単体テストのコードを格納するディレクトリ 
|   `-- integration    : 結合テストのコードを格納するディレクトリ
|-- docs               : ドキュメントを格納するディレクトリ
|   |-- api            : APIドキュメントを格納するディレクトリ
|   `-- user           : ユーザーマニュアルを格納するディレクトリ
|-- config             : 設定ファイルを格納するディレクトリ
|   |-- dev.env        : 開発環境用の環境変数を定義するファイル
|   `-- prod.env       : 本番環境用の環境変数を定義するファイル
`-- build              : ビルドやデプロイに関連するファイルを格納するディレクトリ
    |-- Dockerfile     : Dockerイメージをビルドするための設定ファイル
    `-- scripts        : ビルドやデプロイのスクリプトを格納するディレクトリ
    """
    
    with open("def.md", "w", encoding="utf-8") as file:
        file.write(content)

# ディレクトリ構造を作成
create_directory_structure()

# def.mdファイルを生成
generate_def_md()