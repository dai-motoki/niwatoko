# niwatoko v1.1.2


Anthropic社のドキュメント変数機能をオープンソースで再現し（世界２番目*）、さらにモジュールインポート機能を提供しました（世界初*）


## インストール方法

詳細以下URLを参考にしてください

[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)

1. python, anthropic keyなどが整っている人は以下コマンドで利用できます。

   ```
   pip install niwatoko
   ```

   または、最新版にアップグレードする場合は以下のコマンドを実行します。

   ```
   pip install --upgrade niwatoko
   ```

2. APIキーの設定
- OpenAI APIキーの設定
export OPENAI_API_KEY=sk-xxxxx

- Anthropic APIキーの設定
export ANTHROPIC_API_KEY=sk-xxxxx

- GEMINIプロジェクトの設定
export GEMINI_PROJECT=gemini-xxxxx
export GEMINI_LOCATION=asia-northeast1

- `gemini-1.5-pro`と`gemini-1.5-flash`モデルを追加しました。
  - これらのモデルは画像入力に対応しており、高品質な出力が期待できます。
  - 使用するには、`-m gemini-1.5-pro`または`-m gemini-1.5-flash`オプションを指定します。
- 画像入力モデルを選択するための`-mii`または`--model-input-image`オプションを追加しました。
  - 画像入力に対応したモデル（`openai-gpt4o`、`gemini-1.5-pro`、`gemini-1.5-flash`）から選択できます。
  - デフォルトは`openai-gpt4o`です。



## 練習問題

以下の手順で利用します。
- 事前準備
1. このリポジトリのmainブランチをクローンします。

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. クローンしたディレクトリに移動します。

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.2
   ```

- 実行

1. `test_input.md` ファイルを用意します。このファイルにはテストしたい入力内容を記述します。

2. 以下のコマンドを実行して、`test_input.md` の内容を変換し、`output.md` ファイルに出力します。

   ```
   niwatoko test_input.md -o output.md
   ```

3. 以下のコマンドを実行して、`output.md` の内容をPythonコードに変換し、`output.py` ファイルに出力します。

   ```
   niwatoko output.md -o output.py
   ```

4. 生成された `output.md` および `output.py` ファイルの内容を確認し、期待通りの出力になっているかチェックします。

5. 期待の出力になるまで何度も実行してください。


## アップデート内容

### インポート（引用）機能の追加
- Markdownファイル内で他のファイルの内容を引用できるようになりました。
- これにより、コードの再利用性が向上し、ドキュメントの管理がしやすくなります。
- 引用方法は以下の通りです。
  ```markdown
  - `変数名` = `ファイル形式` [ファイルパス]
  ```
- 例：
  ```markdown
  - `足し算py` = py [./test_import_module_add]
  ```
- この機能は世界初の試みです。
- 鍵かっこ[]のなかに.pyのような拡張子は入れないので注意してください

### ドキュメント変数機能の追加
- Markdownファイル内で変数を定義し、その変数を他の場所で参照できるようになりました。 
- これにより、ドキュメントの可読性と保守性が向上します。
- 変数の定義方法は以下の通りです。
  ```markdown
  `変数名` = 値
  ```
- 変数の参照方法は以下の通りです。
  ```markdown
  `変数名`
  ```
- 例：
  ```markdown
  `プロジェクト名` = py [./test_import_module_add]
  `プロジェクト名` は、自然言語をPythonコードに変換するツールです。
  ```
- この機能は、Anthropic社に次いで世界で2番目の実装です。
