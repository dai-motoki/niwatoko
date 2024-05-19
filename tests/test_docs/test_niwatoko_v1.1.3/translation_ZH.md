中国語への翻訳:

# niwatoko v1.1.3

私たちは、Anthropicのドキュメント変数機能をオープンソース(世界で2番目*)として再現し、モジュールインポート機能(世界初*)を提供しました。

## 更新内容

### インポート(引用)機能の追加
- Markdownファイル内で他のファイルの内容を引用することができるようになりました。
- これにより、コードの再利用性が向上し、ドキュメントの管理が容易になります。

- 引用方法は以下の通りです:
   ```markdown
   - `変数名` = 拡張子 [./ファイルパス(拡張子名削除)]
   - `変数名` = [./ファイルパス]
   ```
- 例:
   ```markdown
    `hello.py` = py [./hello]
    `hello.py` = [./hello.py]
   ```
- この機能は世界初の試みです。
- ファイル拡張子(.py)は角括弧[]の中に含める必要があることに注意してください。

### ドキュメント変数機能の追加
- Markdownファイル内で変数を定義し、その変数を他の場所で参照することができるようになりました。
- これにより、ドキュメントの可読性と保守性が向上します。
- この機能は、Anthropicに続いて世界で2番目の実装です。

## インストール

詳細については以下のURLをご覧ください:
[https://niwatoko2.vercel.app/installation.html](https://niwatoko2.vercel.app/installation.html)


1. Pythonやアンソロピックのキーなどが設定済みの方は、以下のコマンドで使用できます:

   ```
   pip install niwatoko
   ```

   または、最新バージョンにアップグレードするには以下のコマンドを実行してください:
   
   ```
   pip install --upgrade niwatoko
   ```


## 練習問題

以下の手順を使用してください:
- 準備
1. このリポジトリのmainブランチをクローンします。

   ```
   git clone -b main https://github.com/dai-motoki/niwatoko.git
   ```

2. クローンしたディレクトリに移動します。

   ```
   cd niwatoko/tests/test_docs/test_niwatoko_v1.1.3
   ```

- 実行

1. `test_input.md`ファイルを準備します。このファイルには、テストしたい入力内容が記述されています。

```test_input.md
## 引用
- `addition_py` = py [./test_import_module_add]
- `multiplication_py` = py [./test_import_module_multiple]  

## TODO
`addition_py` と `multiplication_py` を日本語のみで要件仕様書に変換してください。
また、必要なテストについても記述してください。
```

2. 以下のコマンドを実行して、`test_input.md`の内容を変換し、`output.md`ファイルに出力します:

   ```
   niwatoko test_input.md -o output.md
   ```

3. 以下のコマンドを実行して、`output.md`の内容をPythonコードに変換し、`output.py`ファイルに出力します:

   ```
   niwatoko output.md -o output.py
   ```

4. 生成された`output.md`と`output.py`ファイルの内容を確認し、出力が期待通りであることを確認します。

5. 期待通りの出力が得られるまで、繰り返し実行します。

