import subprocess
import os
from niwatoko.foundation_model.interpretation.llm.claude import generate_response
from niwatoko.foundation_model.interpretation.llm.gpt import generate_response as gpt_generate_response
from niwatoko.foundation_model.interpretation.llm.gpt import generate_response_gpt4o as gpt_generate_response_gpt4o
import niwatoko
import re
from tqdm import tqdm
import itertools
import threading
import sys
import time
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models
import requests
# OpenAI API Key
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()
# import cv2
# from moviepy.editor import VideoFileClip
# import time
import base64

def main():
    """
    自然言語のソースコードを読み込んで実行する関数。
    コマンドライン引数を解析して処理を実行します。
    """
    my_logger("main関数の開始", level='INFO')
    
    # コマンドライン引数の解析
    args = sys.argv[1:]
    file_path = None
    model = 'claude-haiku'
    model_input_image = 'openai-gpt4o'
    output = None

    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ('-m', '--model'):
            model = args[i + 1]
            my_logger(f"モデルが指定されました: {model}", level='DEBUG')
            i += 1
        elif arg in ('-mii', '--model-input-image'):
            model_input_image = args[i + 1]
            my_logger(f"画像入力モデルが指定されました: {model_input_image}", level='DEBUG')
            i += 1
        elif arg in ('-o', '--output'):
            output = args[i + 1]
            my_logger(f"出力ファイルが指定されました: {output}", level='DEBUG')
            i += 1
        elif arg in ('-v', '--version'):
            try:
                print(f"niwatoko version: {niwatoko.__version__}")
                my_logger(f"バージョン情報: {niwatoko.__version__}", level='INFO')
            except AttributeError:
                print("バージョン情報がniwatokoモジュールに存在しません。")
                my_logger("バージョン情報がniwatokoモジュールに存在しません。", level='ERROR')
            return
        elif arg[0] != '-':
            file_path = arg
            my_logger(f"ファイルパスが指定されました: {file_path}", level='DEBUG')
        else:
            print(f"不明なオプション: {arg}")
            my_logger(f"不明なオプション: {arg}", level='WARNING')
            print_usage()
            return
        i += 1

    if not file_path:
        print("ファイルパスが指定されていません。")
        my_logger("ファイルパスが指定されていません。", level='ERROR')
        print_usage()
        return

    # 処理の開始
    my_logger("処理の開始", level='INFO')
    processed_content = process_imports(file_path, model_input_image)
    my_logger(f"processed_content: {processed_content}", level='DEBUG')
    print("実行中... (Processing...)")

    # ぐるぐるアニメーションを表示するスレッドを開始
    done = False
    spinner = threading.Thread(target=spin, args=(lambda: done,))
    spinner.start()
    my_logger("スピナーを開始", level='INFO')

    while True:
        generated_code = generate_code(model, processed_content)
        my_logger(f"生成されたコード: {generated_code}", level='DEBUG')
        
        # ぐるぐるアニメーションを停止
        done = True
        spinner.join()
        my_logger("スピナーを停止", level='INFO')

        if output:
            with open(output, 'w', encoding="utf-8") as file:
                code_block_start = generated_code.find("```") + 10  # コードブロックの開始位置を見つける
                code_block_end = generated_code.find("```", code_block_start)  # コードブロックの終了位置を見つける
                code_content = generated_code[code_block_start:code_block_end]  # コードブロックの内容を抽出する
                file.write(code_content)  # 抽出したコードをファイルに書き込む
                my_logger(f"生成されたコードを {output} に書き出しました。", level='INFO')
                print(f"生成されたコードを {output} に書き出しました。")
                print(f"Generated code has been written to {output}.")

                # 拡張子がpyの場合のみコードを実行
                if output.endswith('.py'):
                    print("生成されたコードを実行します。")  # 生成されたコードを実行する旨を表示
                    my_logger("生成されたコードを実行します。", level='INFO')
                    exec_globals = {}  # 実行環境のグローバル変数を初期化
                    exec_locals = {}  # 実行環境のローカル変数を初期化
                    try:
                        exec(code_content, exec_globals, exec_locals)  # execを使用して生成されたコードを実行
                        my_logger("生成されたコードの実行が成功しました。", level='INFO')
                        print("生成されたコードの実行が成功しました。")  # 実行成功のメッセージを表示
                        break  # 成功した場合、ループを抜ける
                    except Exception as e:
                        my_logger(f"生成されたコードの実行に失敗しました。エラー: {str(e)}", level='ERROR')
                        print("生成されたコードの実行に失敗しました。")  # 実行失敗のメッセージを表示
                        print("エラー:", str(e))  # エラーメッセージを表示
                        # エラー要因を想定してテキストで出力
                        error_analysis = generate_code(
                            model=model,
                            content=f"以下のエラーが発生しました。考えられる要因を分析してください。\n\nエラー: {str(e)}"
                        )
                        my_logger(f"エラー要因の分析結果: {error_analysis}", level='DEBUG')
                        print("エラー要因の分析結果:", error_analysis)
                        user_input = input("エラーが発生しました。自動修正を試みますか？ (y/n): ")  # 自動修正を試みるかユーザーに確認
                        if user_input.lower() == 'y':
                            # エラー要因の分析結果をプロンプトに追加
                            processed_content += f"\n# エラーが出ました。修正してください: {str(e)}\n# エラー要因の分析:\n{error_analysis}"
                            my_logger("自動修正を試みます。", level='INFO')
                        else:
                            my_logger("自動修正をスキップします。", level='INFO')
                            print("自動修正をスキップします。")  # 自動修正をスキップする旨を表示
                else:
                    break  # Python以外の場合、ループを抜ける

def print_usage():
    """
    使い方の解説を表示する関数
    """
    usage_text = """
    niwatoko コマンドの使い方:

    使用例:
        niwatoko example.md -o example.py
    文法: 
        niwatoko 定義書ファイル名 -o 自然言語出力ファイル名 [-m モデル名] [-mii 画像入力モデル名]
        niwatoko 定義書ファイル名 -o 中間言語ファイル名 [-m モデル名] [-mii 画像入力モデル名]

    オプション:
        -m, --model TEXT                使用するモデルを選択します。 (デフォルト: 'claude-haiku')
        -mii, --model-input-image TEXT  使用する画像入力モデルを選択します。 (デフォルト: 'openai-gpt4o')
        -o, --output PATH               生成されたコードの出力先ファイルを指定します。
        -v, --version                   バージョン情報を表示します。

    モデルの選択肢:
        'openai', 'openai-gpt4o', 'claude', 'claude-sonnet', 'claude-opus', 'claude-haiku', 'gemini-1.5-pro', 'gemini-1.5-flash'

    画像入力モデルの選択肢:（動画の認識はcli.pyのコメントアウトを省くと利用することができます）
        'openai-gpt4o', 'gemini-1.5-pro', 'gemini-1.5-flash'
    """
    my_logger("使用方法を表示", level='INFO')
    print(usage_text)

def generate_code(model, content):
    my_logger(f"generate_code関数の開始 - モデル: {model}", level='INFO')
    if model == 'openai' or model == 'openai-gpt-turbo':
        return gpt_generate_response(
            model="gpt-4-turbo-2024-04-09",
            prompt=content,
            max_tokens=1000,
            temperature=0.5,
        )
    elif model == 'openai-gpt4o':
        return gpt_generate_response_gpt4o(
            prompt=content,
            max_tokens=2048,
            temperature=0.5,
        )
    elif model in ['gemini-1.5-pro', 'gemini-1.5-flash']:
        my_logger(f"Geminiモデルを使用 - モデル: {model}", level='INFO')
        return generate_gemini_response(
            model=model,
            prompt=content,
        )
    else:
        if model == 'claude-sonnet':
            claude_model = 'claude-3-sonnet-20240229'
        elif model == 'claude-opus':
            claude_model = 'claude-3-opus-20240229'
        else:
            claude_model = 'claude-3-haiku-20240307'  # デフォルトはhaiku
        
        my_logger(f"Claudeモデルを使用 - モデル: {claude_model}", level='INFO')
        return generate_response(
            model=claude_model,
            prompt=content,
            max_tokens=4000,
            temperature=0.2,
        )

def spin(done):
    """
    ぐるぐるアニメーションを表示する関数
    Args:
        done (function): アニメーションを停止するかどうかを判定する関数
    """
    my_logger("スピン関数の開始", level='DEBUG')
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done():
            break
        sys.stdout.write(f'\r{c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')
    my_logger("スピン関数の終了", level='DEBUG')

import os
def process_imports(file_path, model_input_image):
    my_logger(f"process_imports関数の開始 - ファイルパス: {file_path}, モデル入力画像: {model_input_image}", level='INFO')
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    output = []
    for line in lines:
        output.extend(process_variable_imports(line))
        if line.startswith('- '):
            parts = line.strip().split(' = ')
            if len(parts) == 2:
                import_path = parts[1].strip()
                if '[' in import_path and not import_path.startswith('['):
                    # ブラケットで囲まれたパスを抽出
                    path_within_brackets = import_path[1:-1]
                    my_logger(f"ブラケット内のパス: {path_within_brackets}", level='DEBUG')
                    # 拡張子を取得
                    extension = path_within_brackets.split('.')[-1]
                    my_logger(f"拡張子: {extension}", level='DEBUG')
                    # 拡張子に応じた処理を行う
                    if extension == 'md':
                        output.extend(process_md_import(import_path, line))
                    elif extension == 'py':
                        output.extend(process_py_import(import_path, line))
                    elif extension == 'rst':
                        output.extend(process_rst_import(import_path, line))
                    else:
                        output.extend(process_other_import(import_path, line))
                elif import_path.startswith('[') and import_path.endswith(']'):
                    # ブラケットで囲まれたパスを抽出
                    import_path = import_path[1:-1]
                    my_logger(f"ブラケット内のパス: {import_path}", level='DEBUG')

                    # パスが存在するか確認
                    if not os.path.exists(import_path):
                        # パスが存在しない場合、新しいパスを設定
                        package_first_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                        my_logger(f"パッケージの最上位ディレクトリ: {package_first_dir}", level='DEBUG')
                        import_path = os.path.join(package_first_dir, f'grimo/grimoires/{import_path}')
                        if not os.path.exists(import_path):
                            error_message = f"{import_path} が見つかりません。\ngrimo install package_name -v version でインストールしてください。"
                            my_logger(error_message, level='ERROR')
                            raise FileNotFoundError(f"\033[91m{error_message}\033[0m")
                    # 拡張子を取得
                    extension = import_path.split('.')[-1]
                    my_logger(f"拡張子: {extension}", level='DEBUG')
                    if extension in ['png', 'jpg', 'jpeg', 'gif']:
                        output.extend(process_image_import(import_path, model_input_image, line))
                    elif extension in ['mp4', 'mov', 'avi']:
                        my_logger("動画ファイルとして処理", level='DEBUG')
                        output.extend(process_video_import(import_path, model_input_image, line))
                    # 拡張子が指定されていない場合、新しい関数を使用して処理
                    else:
                        output.extend(process_no_extension_import(import_path, line))
            else:
                output.append(line)
        else:
            output.append(line)
    
    my_logger("process_imports関数の終了", level='INFO')
    return ''.join(output)

def proc
