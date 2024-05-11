# niwatoko v1.1.1


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





## インストール方法

1. niwatokoをインストールします。

   ```
   pip install niwatoko
   ```

   または、最新版にアップグレードする場合は以下のコマンドを実行します。

   ```
   pip install --upgrade niwatoko
   ```

2. このリポジトリのmainブランチをクローンします。

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

3. クローンしたディレクトリに移動します。

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.1
   ```

## 練習問題

以下の手順で利用します。

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