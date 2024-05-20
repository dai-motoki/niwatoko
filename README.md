# niwatoko - 自然言語プログラミング言語のPythonパッケージ

## 1. 目的
niwatoko は、自然言語でプログラミングを行うことができる新しいプログラミング言語です。このプロジェクトの目的は、niwatoko のPythonパッケージを開発し、ユーザーが自然言語を使ってプログラムを記述し、実行できるようにすることです。パッケージには、自然言語処理のための認識系AIと、プログラムの出力を生成するための生成AI（テキスト生成や画像生成）が組み込まれます。

## 2. パッケージの基本構造
```
niwatoko/
├── niwatoko/
│   ├── __init__.py
│   ├── parser.py
│   ├── interpreter.py
│   ├── foundation_model/
│   │   ├── recognition/
│   │   │   ├── stt/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── openai.py
│   │   │   │   └── claude.py
│   │   │   ├── vision/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── openai.py
│   │   │   │   └── claude.py
│   │   ├── interpretation/
│   │   │   ├── llm/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── openai.py
│   │   │   │   └── claude.py
│   │   │   ├── code/
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   ├── generation/
│   │   │   ├── image/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── openai.py
│   │   │   │   └── claude.py
│   │   │   ├── tts/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── openai.py
│   │   │   │   └── claude.py
│   └── utils/
│       ├── __init__.py
│       └── ...
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_interpreter.py
│   ├── foundation_model/
│   │   ├── recognition/
│   │   │   ├── test_stt.py
│   │   │   └── test_vision.py
│   │   ├── interpretation/
│   │   │   ├── test_llm.py
│   │   │   └── test_code.py
│   │   └── generation/
│   │       ├── test_image.py
│   │       └── test_tts.py
│   ├── test_docs/
│   │   ├── test_doc1.md
│   │   ├── test_doc2.md
│   │   └── test_doc3.md
│   └── ...
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── ...
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/
    ├── ci.yml
    └── cd.yml
```

- `niwatoko/`: パッケージのメインディレクトリ。パーサー、インタープリター、AIモジュールなどが含まれます。
- `tests/`: テストコードを格納するディレクトリ。
- `docs/`: Sphinxを使用して生成されるドキュメントのソースファイルを格納するディレクトリ。
- `README.md`: パッケージの概要、インストール方法、使用方法などを説明するファイル。
- `LICENSE`: パッケージのライセンスを記載するファイル。
- `setup.py`: パッケージのメタデータとインストール方法を定義するファイル。
- `requirements.txt`: パッケージが依存する外部ライブラリを記載するファイル。
- `Dockerfile`: Dockerイメージのビルド手順を記述するファイル。
- `docker-compose.yml`: 複数のDockerコンテナを定義・実行するための設定ファイル。
- `.github/workflows/`: GitHub ActionsによるCI/CDワークフローの設定ファイルを格納するディレクトリ。
