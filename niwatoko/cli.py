import subprocess
import click
import os
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


    with open(file_path, 'r', encoding = "utf-8") as file:

        natural_language_code = file.read()
    
    prompt = f"{natural_language_code}"
    print(natural_language_code)
    print("=================================")

    if model == 'openai':
        generated_code = gpt_generate_response(
            model="gpt-4-turbo-2024-04-09",
            prompt=natural_language_code,
            max_tokens=1000,
            temperature=0.5,
        )
    elif model == 'claude':
        generated_code = generate_response(
            # model='claude-3-sonnet-20240229',
            model='claude-3-haiku-20240307',
            prompt=prompt,
            max_tokens=4000,
            temperature=0.2,
        )
    else:
        raise ValueError(f"無効なモデル: {model}")

    if output:
        with open(output, 'w', encoding = "utf-8") as file:
            file.write(generated_code)
        
        if input(f"生成されたコードを {output} に書き出しました。実行しますか？(y/n)\n").lower() == "y":
            subprocess.run(["python", output])
    else:
        print("生成されたコードの保存先が指定されていないため、自動実行します。")
        output = os.path.dirname(niwatoko.__file__) + "/temp.py"
        with open(output, 'w', encoding = "utf-8") as file:
            file.write(generated_code.replace("`","").replace("python",""))
        subprocess.run(["python", output])



#     match = re.search(r'version=[\'\"](.+?)[\'\"]', content)
#     if match:
#         version = match.group(1)
#     else:
#         raise ValueError("バージョン情報が見つかりませんでした。")

#     return version


