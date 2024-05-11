import click
import os
from .foundation_model.interpretation.llm.claude import generate_response
from .foundation_model.interpretation.llm.gpt import generate_response as gpt_generate_response
from ._version import __version__
import itertools
import threading
import sys
import time


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
            print(f"niwatoko version: {__version__}")
        except AttributeError:
            print("バージョン情報がniwatokoモジュールに存在しません。")
        return
    if not file_path:
        print("ファイルパスが指定されていません。")
        return

    processed_content = process_imports(file_path)

    print("実行中...")

    # ぐるぐるアニメーションを表示するスレッドを開始
    done = False
    spinner = threading.Thread(target=spin, args=(lambda: done,))
    spinner.start()

    if model == 'openai':
        generated_code = gpt_generate_response(
            model="gpt-4-turbo-2024-04-09",
            prompt=processed_content,
            max_tokens=1000,
            temperature=0.5,
        )
    elif model == 'claude':
        generated_code = generate_response(
            model='claude-3-haiku-20240307',
            prompt=processed_content,
            max_tokens=4000,
            temperature=0.2,
        )
    else:
        raise ValueError(f"無効なモデル: {model}")

    # ぐるぐるアニメーションを停止
    done = True
    spinner.join()

    if output:
        with open(output, 'w', encoding="utf-8") as file:
            file.write(generated_code)
            print(f"\n生成されたコードを {output} に書き出しました。")


def spin(done):
    """
    ぐるぐるアニメーションを表示する関数

    Args:
        done (function): アニメーションを停止するかどうかを判定する関数
    """
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done():
            break
        sys.stdout.write(f'\r{c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')


def process_imports(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    output = []
    for line in lines:
        if line.startswith('- '):
            parts = line.strip().split(' = ')
            if len(parts) == 2:
                import_path = parts[1].strip()
                if '[' in import_path and not import_path.startswith('['):
                    # ブラケットで囲まれたパスを抽出
                    path_within_brackets = import_path[import_path.index(
                        '[') + 1:import_path.index(']')]
                    # 拡張子を取得
                    extension = path_within_brackets.split('.')[-1]
                    # print(extension)
                    # 拡張子に応じた処理を行う
                    if extension == 'md':
                        output.extend(process_md_import(import_path, line))
                    elif extension == 'py':
                        output.extend(process_py_import(import_path, line))
                    elif extension == 'rst':
                        output.extend(process_rst_import(import_path, line))
                    else:
                        # その他の拡張子の場合
                        output.extend(process_other_import(import_path, line))
                else:
                    # 拡張子が指定されていない場合、新しい関数を使用して処理
                    output.extend(
                        process_no_extension_import(import_path, line))
            else:
                output.append(line)
        else:
            output.append(line)

    return ''.join(output)


def process_no_extension_import(import_path, line):
    """
    Markdownファイルのインポートを処理する関数

    Args:
        import_path (str): インポートするファイルのパス
        line (str): インポート文の行

    Returns:
        list: 処理後の出力行のリスト
    """
    # print(import_path)
    import_path = import_path[1:-1]
    import_content = get_file_content(import_path)
    # print(import_content)
    return [line, '```\n', import_content, '```\n']


def process_md_import(import_path, line):
    """
    Markdownファイルのインポートを処理する関数

    Args:
        import_path (str): インポートするファイルのパス
        line (str): インポート文の行

    Returns:
        list: 処理後の出力行のリスト
    """
    import_path = import_path[4:-1] + '.md'  # 拡張子を追加
    import_content = get_file_content(import_path)
    return [line, '```\n', import_content, '```\n']


def process_py_import(import_path, line):
    """
    Pythonファイルのインポートを処理する関数

    Args:
        import_path (str): インポートするファイルのパス
        line (str): インポート文の行

    Returns:
        list: 処理後の出力行のリスト
    """
    import_path = import_path[4:-1] + '.py'  # 拡張子を追加
    import_content = get_file_content(import_path)
    return [line, '```python\n', import_content, '```\n']


def process_rst_import(import_path, line):
    """
    reStructuredTextファイルのインポートを処理する関数

    Args:
        import_path (str): インポートするファイルのパス
        line (str): インポート文の行

    Returns:
        list: 処理後の出力行のリスト
    """
    import_path = import_path[5:-1] + '.rst'  # 拡張子を追加
    import_content = get_file_content(import_path)
    return [line, '```rst\n', import_content, '```\n']


def process_other_import(import_path, line):
    """
    md, py, rst以外の拡張子のインポートを処理する関数

    Args:
        import_path (str): インポートするファイルのパス
        line (str): インポート文の行

    Returns:
        list: 処理後の出力行のリスト
    """
    extension = import_path.split(
        '['
    )[0].strip()  # 文字列の一番左から [ の一文字前までを拡張子として取得
    import_path = import_path.split(
        '['
    )[1].split(']')[0].strip() + '.' + extension  # [ と ] の間にあるパスに拡張子を追加
    import_content = get_file_content(import_path)
    return [line, f'```{extension}\n', import_content, '```\n']


def get_file_content(file_path):
    # print(file_path)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        error_message = f"ファイルが見つかりません: {file_path}"
        # print(error_message)
        raise FileNotFoundError(error_message)
