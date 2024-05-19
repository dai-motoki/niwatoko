### 実装計画:
1. pytest や unittest を用いたテストケースの作成
2. CLIコマンドごとの動作確認テスト
3. エラーハンドリングのテストケース追加
4. CI/CDパイプラインへの組み込み

プロジェクトの構成部分としてCLI機能が正しく動作することが重要です。CLIテストコードを実装することで、以下の利点があります:
- 実装されたCLI機能の動作確認
- 将来的な機能追加や修正に向けた信頼性の向上
- バージョンアップ時の回帰テストの自動化


このイシューの完了により、安定したCLI操作が保証され、ユーザー体験が改善されます。

### 該当部分は以下、以下を検証したい。


import click
import os
import openai
from niwatoko.foundation_model.interpretation.llm.claude import generate_response
from niwatoko.foundation_model.interpretation.llm.gpt import generate_response as gpt_generate_response
import niwatoko

@click.command()
@click.argument('file_path', type=click.Path(exists=True), required=False)
@click.option('-m', '--model', type=click.Choice(['openai', 'claude']), default='claude', help='使用するモデルを選択します。')
@click.option('-o', '--output', type=click.Path(), help='生成されたコードの出力先ファイルを指定します。')
@click.option('-v', '--version',  is_flag=True, help='バージョン情報を表示します。')

def main(file_path, model, output, version):
    """
    自然言語のソースコードを読み込んで実行するコマンドラインインターフェース。

    Args:
        file_path (str): 自然言語のソースコードが書かれたファイルのパス。
        model (str): 使用するモデル（OpenAIまたはClaude）。
        output (str): 生成されたコードの出力先ファイルのパス。
        version (bool): バージョン情報を表示するかどうか。
    """
    if version:
        try:
            print(f"niwatoko version: {niwatoko.__version__}")
        except AttributeError:
            print("バージョン情報がniwatokoモジュールに存在しません。")
        return
    if not file_path:
        print("ファイルパスが指定されていません。")
        return

    with open(file_path, 'r') as file:
        natural_language_code = file.read()

    if model == 'openai':
        generated_code = gpt_generate_response(
            model="gpt-4-turbo-2024-04-09",
            prompt=natural_language_code,
            max_tokens=1000,
            temperature=0.5,
        )
    elif model == 'claude':
        prompt = f"{natural_language_code}"
        print(natural_language_code)
        print("=================================")
        generated_code = generate_response(
            model='claude-3-sonnet-20240229',
            prompt=prompt,
            max_tokens=4000,
            temperature=0.2,
        )
    else:
        raise ValueError(f"無効なモデル: {model}")

    if output:
        with open(output, 'w') as file:
            file.write(generated_code)
            print(f"生成されたコードを {output} に書き出しました。")




## 実行

pytestコードを記述すること
os を利用して niwatokoコマンドのCLIでのテストを行うこと
niwatoko sample.md

あと、1つ1つ確認できるように全てのテストは細かく関数にすること
とか

出力先はpythonファイルです。

解説はコメントアウト

## チェック

解説
```
`code`
```
解説


これは

コードブロック絶対入れるな
`code`
コードブロック絶対入れるな
# 解説 （コメントアウトでかけ）

で出力


