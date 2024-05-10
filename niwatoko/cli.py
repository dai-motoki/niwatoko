import subprocess
import click
import os
from niwatoko.foundation_model.interpretation.llm.claude import generate_response
from niwatoko.foundation_model.interpretation.llm.gpt import generate_response as gpt_generate_response
import niwatoko
import re

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

    # input_file = 'niwatoko.md'
    # output_file = '全体ファイル.md'

    processed_content = process_imports(file_path)


    print(processed_content)

    if model == 'openai':
        generated_code = gpt_generate_response(
            model="gpt-4-turbo-2024-04-09",
            prompt=processed_content,
            max_tokens=1000,
            temperature=0.5,
        )
    elif model == 'claude':
        generated_code = generate_response(
            # model='claude-3-sonnet-20240229',
            model='claude-3-haiku-20240307',
            prompt=processed_content,
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


import os

def process_imports(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    output = []
    for line in lines:
        print(f"Processing line: {line.strip()}")  # デバッグ用のprint
        if line.startswith('- '):
            parts = line.strip().split(' = ')
            if len(parts) == 2:
                import_path = parts[1].strip()
                if import_path.startswith('md ['):
                    import_path = import_path[4:-1] + '.md'  # 拡張子を追加
                    print(f"Importing markdown file: {import_path}")  # デバッグ用のprint
                    import_content = get_file_content(import_path)
                    output.append(line)
                    output.append('```\n')
                    output.append(import_content)
                    output.append('```\n')
                elif import_path.startswith('py ['):
                    import_path = import_path[4:-1] + '.py'  # 拡張子を追加
                    print(f"Importing Python file: {import_path}")  # デバッグ用のprint
                    import_content = get_file_content(import_path)
                    output.append(line)
                    output.append('```python\n')
                    output.append(import_content)
                    output.append('```\n')
                else:
                    print(f"Unsupported import type: {import_path}")  # デバッグ用のprint
                    output.append(line)
            else:
                print(f"Invalid import statement: {line.strip()}")  # デバッグ用のprint
                output.append(line)
        else:
            print(f"Regular line: {line.strip()}")  # デバッグ用のprint
            output.append(line)
    
    print("Processed content:")  # デバッグ用のprint
    print(''.join(output))  # デバッグ用のprint
    
    return ''.join(output)

def get_file_content(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        print(f"File not found: {file_path}")  # デバッグ用のprint
        return f"ファイルが見つかりません: {file_path}"

# # 使用例
# input_file = 'niwatoko.md'
# output_file = '全体ファイル.md'

# processed_content = process_imports(input_file)

# with open(output_file, 'w') as file:
#     file.write(processed_content)