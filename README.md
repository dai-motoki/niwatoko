# 抽象プログラミング言語 にわとこ

## 利用方法は以下URLをチェックしてください。
https://niwatoko2.vercel.app/


## 以下は開発者向け

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

## 3. setup.pyの書き方
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="niwatoko",
    version="0.1.0",
    description="A natural language programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/niwatoko",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "nltk",
        "tensorflow",
        "torch",
        "transformers",
        "pillow",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
```

- `name`: パッケージ名を指定します。
- `version`: パッケージのバージョンを指定します。
- `description`: パッケージの短い説明を記載します。
- `long_description`: パッケージの詳細な説明を記載します。通常、README.mdの内容を指定します。
- `author`: 作者名を記載します。
- `author_email`: 作者のメールアドレスを記載します。
- `url`: パッケージのWebサイトやリポジトリのURLを指定します。
- `packages`: パッケージに含めるPythonモジュールを指定します。`find_packages()`を使用して自動的に検出できます。
- `install_requires`: パッケージが依存する外部ライブラリを指定します。

## 4. __init__.pyの役割
```python
__version__ = "0.1.0"

from .parser import parse
from .interpreter import interpret
```

- `__init__.py`は、パッケージの初期化処理を行うファイルです。
- `__version__`変数を定義して、パッケージのバージョンを指定します。
- パッケージの公開APIとなる関数やクラスを`__init__.py`でimportすることで、ユーザーがパッケージを使用しやすくなります。

## 5. README.mdの書き方
```markdown
# niwatoko

niwatoko is a natural language programming language that allows users to write programs using natural language. It is implemented as a Python package and includes recognition AI for natural language processing and generative AI for program output (text and image generation).

## Installation

To install niwatoko, use pip:

```
pip install niwatoko
```

## Usage

Here's a simple example of how to use niwatoko:

```python
from niwatoko import parse, interpret

program = """
Create a function that takes two numbers as input and returns their sum.
"""

ast = parse(program)
result = interpret(ast)
print(result)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## Support

If you have any questions or need support, please open an issue on the [GitHub repository](https://github.com/yourusername/niwatoko/issues).
```

- パッケージの概要を説明します。
- インストール方法を記載します。
- 使用方法を具体的なコード例とともに説明します。
- ライセンスについて言及し、LICENSEファイルへのリンクを貼ります。
- 貢献方法について説明し、CONTRIBUTING.mdファイルへのリンクを貼ります。
- サポート方法を記載し、GitHubのissueページへのリンクを貼ります。

## 6. LICENSEファイル
- LICENSEファイルは、パッケージのライセンスを明記するためのファイルです。
- 主要なオープンソースライセンスには以下のようなものがあります。
  - MIT License: 非常に寛容なライセンスで、商用利用、修正、配布、私的利用が認められています。
  - Apache License 2.0: 商用利用、修正、配布、特許の使用が認められています。ライセンス条文の提供が必要です。
  - GNU General Public License (GPL): 強いコピーレフトライセンスで、派生物はGPLで公開する必要があります。
  - BSD License: MITライセンスと同様に寛容なライセンスですが、ライセンス条文の提供が必要です。

## 7. パッケージのバージョン管理
- セマンティックバージョニングに基づいて、MAJOR.MINOR.PATCH形式でバージョンを表現します。
- APIの互換性が損なわれる変更を行った場合は、MAJORバージョンを上げます。
- 後方互換性を保ちつつ機能を追加した場合は、MINORバージョンを上げます。
- バグ修正などの小さな変更は、PATCHバージョンを上げます。

## 8. テストの書き方
- テストファイルの命名規則は、`test_*.py`または`*_test.py`とします。
- テストクラスは、`unittest.TestCase`を継承して定義します。
- テストメソッドの命名規則は、`test_`で始めます。
- `assert`メソッドを使用して、期待する結果と実際の結果を比較します。
- `coverage.py`などのツールを使用して、テストのカバレッジを測定します。
- CLIコマンドの実行結果をキャプチャして、期待する出力と比較するテストを作成します。
- 異なるコマンドラインオプションを指定した場合のテストを作成します。
- エラー処理のテスト（不正な引数を渡した場合など）を作成します。

## 9. ドキュメントの作成方法
- Sphinxを使用してドキュメントを作成します。
- `sphinx-quickstart`コマンドを実行して、Sphinxプロジェクトを作成します。
- reStructuredText記法を使用して、ドキュメントのソースファイルを作成します。
- `"""docstring"""`を使用して、モジュール、クラス、関数のドキュメントを記述します。
- `conf.py`ファイルでSphinxの設定を行います。
- `make html`コマンドを実行して、HTMLドキュメントを生成します。

## 10. Docker化とCI/CDの設定
- `Dockerfile`を作成して、アプリケーションのDockerイメージをビルドします。
- `docker-compose.yml`ファイルを作成して、複数のDockerコンテナを定義し、実行します。
- DockerイメージをビルドしてDocker Hubなどのコンテナレジストリにプッシュします。
- GitHub Actionsを使用して、CI/CDパイプラインを設定します。
  - `ci.yml`ファイルでテスト、リンター、コードフォーマッターなどを実行します。
  - `cd.yml`ファイルでDockerイメージのビルドとプッシュ、デプロイメントを自動化します。

## 11. WebアプリケーションのUI設定
- Streamlitを使用してWebアプリケーションのUIを設定します。
  - `streamlit`ライブラリをインストールします。
  - `app.py`ファイルを作成し、Streamlitアプリケーションを定義します。
  - UIコンポーネントを配置し、入力を受け取り、処理結果を表示します。
- Gradioを使用してWebアプリケーションのUIを設定します。
  - `gradio`ライブラリをインストールします。
  - `app.py`ファイルを作成し、Gradioアプリケーションを定義します。
  - UIコンポーネントを配置し、入力を受け取り、処理結果を表示します。

パッケージの開発にあたっては、PEP 8などのPythonコーディング規約に従い、可読性と保守性を重視します。また、適切なモジュール化とオブジェクト指向設計を行い、拡張性と再利用性を高めます。

パッケージの公開には、PyPIを利用します。`setup.py`ファイルを適切に設定し、`python setup.py sdist bdist_wheel`コマンドでパッケージを作成した後、`twine upload dist/*`コマンドでPyPIにアップロードします。

CI/CDの設定には、GitHub Actionsを使用します。`.github/workflows/`ディレクトリにYAMLファイルを作成し、テスト、リンター、コードフォーマッター、Dockerイメージのビルドとプッシュ、デプロイメントなどの自動化タスクを定義します。



## メモ


はい、VercelでSphinxのドキュメントを公開することができます。Vercelは静的サイトホスティングに特化したサービスで、Sphinxのような静的サイトジェネレーターとの相性が良いです。

Vercelを使ってSphinxドキュメントを公開する手順は以下の通りです。

1. Sphinxプロジェクトをビルドする
```bash
sphinx-build -b html . _build/html && open _build/html/index.html
```

2. Vercel用の設定ファイル `vercel.json` をプロジェクトルートに作成する
```json
{
  "version": 2,
  "builds": [
    {
      "src": "*.html",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/_build/html/$1"
    }
  ]
}
```

この設定では、`_build/html` ディレクトリ以下の静的ファイルを公開するように指定しています。

3. Vercelにプロジェクトをデプロイする  
VercelのCLIをインストールし、プロジェクトルートで以下のコマンドを実行します。
```bash
$ vercel --prod
```
Vercelのコマンドが見つからないというエラーが発生していますね。
VercelのCLIがインストールされていない可能性があります。

以下の手順でVercel CLIをインストールしてください。

1. Node.jsとnpmがインストールされていることを確認する  
Vercel CLIはNode.jsとnpmを使用するため、あらかじめインストールしておく必要があります。ターミナルで以下のコマンドを実行し、バージョンが表示されればインストール済みです。
```bash
$ node -v
$ npm -v
```


2. Vercel CLIをインストールする  
npmを使ってVercel CLIをグローバルにインストールします。
```bash
$ npm install -g vercel
```


3. インストールを確認する  
インストールが完了したら、以下のコマンドでバージョンを確認します。
```bash
$ vercel --version
```


バージョンが表示されれば、Vercel CLIのインストールは成功です。

4. Vercelにログインする  
Vercel CLIを使ってデプロイするには、Vercelアカウントにログインする必要があります。以下のコマンドを実行し、メールアドレスとパスワードを入力してログインします。
```bash
$ vercel login
```


以上の手順でVercel CLIをインストールし、ログインができたら、再度 `vercel --prod` コマンドを実行してデプロイしてみてください。
Vercel CLIが正しくインストールされていれば、デプロイが開始されるはずです。
すると、プロジェクトがVercelにデプロイされ、割り当てられたURLが表示されます。

4. 自動デプロイの設定（オプション）  
VercelはGitHubなどのリポジトリと連携して、pushされたら自動でデプロイすることもできます。Vercelのダッシュボードからプロジェクトの設定を行うことで簡単に自動デプロイを設定できます。

以上の手順により、VercelでSphinxドキュメントを公開することができます。
Vercelは無料プランでも十分な機能を提供しているため、手軽にSphinxドキュメントをホスティングするのに適したサービスと言えます。