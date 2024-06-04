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
from vertexai.generative_models import GenerativeModel, Part, FinishReason
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
            i += 1
        elif arg in ('-mii', '--model-input-image'):
            model_input_image = args[i + 1]
            i += 1
        elif arg in ('-o', '--output'):
            output = args[i + 1]
            i += 1
        elif arg in ('-v', '--version'):
            try:
                print(f"niwatoko version: {niwatoko.__version__}")
            except AttributeError:
                print("バージョン情報がniwatokoモジュールに存在しません。")
            return
        elif arg[0] != '-':
            file_path = arg
        else:
            print(f"不明なオプション: {arg}")
            print_usage()
            return
        i += 1

    if not file_path:
        print("ファイルパスが指定されていません。")
        print_usage()
        return

    # 処理の開始
    processed_content = process_imports(file_path, model_input_image)
    # print("processed_content:", processed_content)
    print("実行中... (Processing...)")

    # ぐるぐるアニメーションを表示するスレッドを開始
    done = False
    spinner = threading.Thread(target=spin, args=(lambda: done,))
    spinner.start()

    while True:
        generated_code = generate_code(model, processed_content)
        
        # ぐるぐるアニメーションを停止
        done = True
        spinner.join()

        if output:
            with open(output, 'w', encoding="utf-8") as file:
                code_block_start = generated_code.find("```") + 10  # コードブロックの開始位置を見つける
                code_block_end = generated_code.find("```", code_block_start)  # コードブロックの終了位置を見つける
                code_content = generated_code[code_block_start:code_block_end]  # コードブロックの内容を抽出する
                file.write(code_content)  # 抽出したコードをファイルに書き込む
                print(f"生成されたコードを {output} に書き出しました。")
                print(f"Generated code has been written to {output}.")
                print("生成されたコードを実行します。")  # 生成されたコードを実行する旨を表示
                exec_globals = {}  # 実行環境のグローバル変数を初期化
                exec_locals = {}  # 実行環境のローカル変数を初期化
            try:
                exec(code_content, exec_globals, exec_locals)  # execを使用して生成されたコードを実行
                print("生成されたコードの実行が成功しました。")  # 実行成功のメッセージを表示
                break  # 成功した場合、ループを抜ける
            except Exception as e:
                print("生成されたコードの実行に失敗しました。")  # 実行失敗のメッセージを表示
                print("エラー:", str(e))  # エラーメッセージを表示
                # エラー要因を想定してテキストで出力
                error_analysis = generate_code(
                    model=model,
                    content=f"以下のエラーが発生しました。考えられる要因を分析してください。\n\nエラー: {str(e)}"
                )
                print("エラー要因の分析結果:", error_analysis)
                user_input = input("エラーが発生しました。自動修正を試みますか？ (y/n): ")  # 自動修正を試みるかユーザーに確認
                if user_input.lower() == 'y':
                    # エラー要因の分析結果をプロンプトに追加
                    processed_content += f"\n# エラーが出ました。修正してください: {str(e)}\n# エラー要因の分析:\n{error_analysis}"
                else:
                    print("自動修正をスキップします。")  # 自動修正をスキップする旨を表示


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
    print(usage_text)

def generate_code(model, content):
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
        print("model:", model)
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
        
        print("model:", claude_model)
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
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done():
            break
        sys.stdout.write(f'\r{c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')

import os
def process_imports(file_path, model_input_image):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    output = []
    for line in lines:
        output.extend(process_variable_imports(line))
        if line.startswith('- '):
            parts = line.strip().split(' = ')
            if len(parts) == 2:
                import_path = parts[1].strip()
                # print('import_path:', import_path)
                if '[' in import_path and not import_path.startswith('['):
                    # ブラケットで囲まれたパスを抽出
                    path_within_brackets = import_path[1:-1]
                    # print("ブラケット内のパス:", path_within_brackets)  # デバッグ用print
                    # 拡張子を取得
                    extension = path_within_brackets.split('.')[-1]
                    # print("拡張子:", extension)  # デバッグ用print
                    # 拡張子に応じた処理を行う
                    if extension == 'md':
                        # print("Markdownファイルとして処理")  # デバッグ用print
                        # print(import_path)
                        output.extend(process_md_import(import_path, line))
                    elif extension == 'py':
                        # print("Pythonファイルとして処理")  # デバッグ用print
                        output.extend(process_py_import(import_path, line))
                    elif extension == 'rst':
                        # print("reStructuredTextファイルとして処理")  # デバッグ用print
                        output.extend(process_rst_import(import_path, line))
                    else:
                        # その他の拡張子の場合
                        # print("その他のファイルタイプとして処理")  # デバッグ用print
                        output.extend(process_other_import(import_path, line))
                elif import_path.startswith('[') and import_path.endswith(']'):
                    # ブラケットで囲まれたパスを抽出
                    path_within_brackets = import_path[1:-1]
                    # print("ブラケット内のパス:", path_within_brackets)  # デバッグ用print
                    # 拡張子を取得
                    extension = path_within_brackets.split('.')[-1]
                    # print("拡張子:", extension)  # デバッグ用print
                    if extension in ['png', 'jpg', 'jpeg', 'gif']:
                        output.extend(process_image_import(import_path, model_input_image, line))

                    elif extension in ['mp4', 'mov', 'avi']:
                        print("動画ファイルとして処理")  # デバッグ用print
                        output.extend(process_video_import(import_path, model_input_image, line))
                    # 拡張子が指定されていない場合、新しい関数を使用して処理
                    else:
                        # print("拡張子が指定されていないため、process_no_extension_importを使用")  # デバッグ用print
                        output.extend(process_no_extension_import(import_path, line))
            else:
                output.append(line)
        else:
            output.append(line)
    
    return ''.join(output)
def process_variable_imports(line):
    """
    {{}}で囲まれた変数のインポートを処理する関数

    Args:
        line (str): ファイルの行

    Returns:
        list: 処理後の出力行のリスト
    """
    output = []
    if '{{' in line and '}}' in line:
        # {{ }} で囲まれた変数を抽出
        variable = line[line.index('{{') + 2:line.index('}}')]
        # 変数名を小文字に変換し、拡張子.mdを追加
        import_path = variable.lower() + '.md'
        # 同一階層内のファイルの内容を取得
        import_content = get_file_content(import_path)
        output.extend([line, '```\n', import_content, '```\n'])
    return output

def process_no_extension_import(import_path, line):
    """
    拡張子が指定されていないインポートを処理する関数

    Args:
        import_path (str): インポートするファイルのパス
        line (str): インポート文の行

    Returns:
        list: 処理後の出力行のリスト
    """
    import_path = import_path[1:-1]
    import_content = get_file_content(import_path)
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
    # print(import_path)
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
    extension = import_path.split('[')[0].strip()  # 文字列の一番左から [ の一文字前までを拡張子として取得
    import_path = import_path.split('[')[1].split(']')[0].strip() + '.' + extension  # [ と ] の間にあるパスに拡張子を追加
    import_content = get_file_content(import_path)
    return [line, f'```{extension}\n', import_content, '```\n']

def process_image_import(import_path, model_input_image, line):
    """
    画像ファイルのインポートを処理する関数

    Args:
        import_path (str): インポートするファイルのパス
        line (str): インポート文の行

    Returns:
        list: 処理後の出力行のリスト
    """
    import_path = import_path[1:-1]
    if model_input_image == 'openai-gpt4o':
        recognized_text = recognize_image_text_gpt4o(import_path)
    elif model_input_image in ['gemini-1.5-pro', 'gemini-1.5-flash']:
        recognized_text = recognize_image_text_gemini(model_input_image, import_path)
    else:
        recognized_text = "指定された画像入力モデルがサポートされていません。"
    return [line, '```\n', recognized_text, '```\n']

def process_video_import(import_path, model_input_image, line):
    """
    動画ファイルのインポートを処理する関数

    Args:
        import_path (str): インポートするファイルのパス
        line (str): インポート文の行

    Returns:
        list: 処理後の出力行のリスト
    """

    import_path = import_path[1:-1]
    if model_input_image == 'openai-gpt4o':
        recognized_text = recognize_video_text_gpt4o(import_path)
    elif model_input_image in ['gemini-1.5-pro', 'gemini-1.5-flash']:
        recognized_text = recognize_video_text_gemini(model_input_image, import_path)
    else:
        recognized_text = "指定された動画入力モデルがサポートされていません。"
    return [line, '```\n', recognized_text, '```\n']

def get_file_content(file_path):
    # print(file_path)
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            return file.read().decode('utf-8')
    else:
        error_message = f"ファイルが見つかりません: {file_path}"
        # print(error_message)
        raise FileNotFoundError(error_message)


# OpenAI APIキーを環境変数から取得
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI APIキーが設定されていません。")
def encode_image(image_path):
    """
    画像ファイルをBase64エンコードする関数

    Args:
        image_path (str): 画像ファイルのパス

    Returns:
        str: Base64エンコードされた画像データ
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def recognize_image_text_gpt4o(image_path):
    """
    画像ファイルからテキストを認識する関数

    Args:
        image_path (str): 画像ファイルのパス

    Returns:
        str: 認識されたテキスト
    """
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "この画像について限界まで詳細に説明してください lang ja"
                        # "text": "この画像をOCRしてください文字のみ lang ja"
                        # "text": "図の全ての依存関係を正確に説明してください"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 2000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    content = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
    # print(content)
    # print('')

    return content


# def recognize_video_text_gpt4o(video_path, seconds_per_frame=1):
#     """
#     動画ファイルからフレームを抽出し、テキストのサマリーを生成する関数

#     Args:
#         video_path (str): 動画ファイルのパス
#         seconds_per_frame (int): フレームを抽出する間隔（秒）

#     Returns:
#         str: 動画のテキストサマリー
#     """
#     import tqdm

#     base64Frames = []
#     base_video_path, _ = os.path.splitext(video_path)

#     video = cv2.VideoCapture(video_path)
#     total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
#     fps = video.get(cv2.CAP_PROP_FPS)
#     frames_to_skip = int(fps * seconds_per_frame)
#     curr_frame = 0

#     # 指定された間隔でフレームを抽出
#     with tqdm.tqdm(total=total_frames, desc="フレーム抽出中") as pbar:
#         while curr_frame < total_frames - 1:
#             video.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
#             success, frame = video.read()
#             if not success:
#                 break
#             _, buffer = cv2.imencode(".jpg", frame)
#             base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
#             curr_frame += frames_to_skip
#             pbar.update(frames_to_skip)
#     video.release()

#     # 動画から音声を抽出
#     audio_path = f"{base_video_path}.mp3"
#     clip = VideoFileClip(video_path)
#     if clip.audio is not None:
#         clip.audio.write_audiofile(audio_path, bitrate="32k")
#         clip.audio.close()
#         print(f"音声を抽出: {audio_path}")
#     else:
#         print("音声が見つかりませんでした。")
#     clip.close()

#     print(f"抽出されたフレーム数: {len(base64Frames)}")

#     # 抽出したフレームと音声を使用してテキストのサマリーを生成
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }

#     # 実行中のバーを追加
#     with tqdm.tqdm(total=1, desc="APIリクエスト送信中") as pbar:
#         payload = {
#             "model": "gpt-4o",
#             "messages": [
#                 {
#                     "role": "system",
#                     # "content": "You are generating a video summary. Please provide a summary of the video. Respond in Markdown."
#                     "content": "この動画について限界まで詳細に説明してください lang ja"
#                 },
#                 {
#                     "role": "user",
#                     "content": [
#                         "These are the frames from the video.",
#                         *map(lambda x: {"type": "image_url", 
#                                         "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, base64Frames)
#                     ]
#                 }
#             ],
#             "max_tokens": 4095
#         }
#         pbar.update(1)
#     response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#     summary = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
#     # print(summary)
#     # print('')

#     return summary





def initialize_gemini_model(model):
    """
    Geminiモデルを初期化する共通関数

    Args:
        model (str): 使用するGeminiモデルの名前

    Returns:
        GenerativeModel: 初期化されたGeminiモデル
    """
    # model名に -review-0514 を追加
    model = f"{model}-preview-0514"
    
    # 環境変数からプロジェクトとロケーションを取得
    from dotenv import load_dotenv
    load_dotenv()

    project = os.getenv("GEMINI_PROJECT")
    location = os.getenv("GEMINI_LOCATION")
    
    # Vertex AIの初期化
    vertexai.init(project=project, location=location)
    return GenerativeModel(model)

def recognize_image_text_gemini(model, image_path):
    """
    Geminiモデルを使用して画像認識を行う関数

    Args:
        model (str): 使用するGeminiモデルの名前
        image_path (str): 画像ファイルのパス

    Returns:
        str: 生成されたテキスト
    """
    model = initialize_gemini_model(model)

    # 画像ファイルをBase64エンコード
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    # 画像データをPartオブジェクトとして作成
    image1 = Part.from_data(
        mime_type="image/jpeg",
        data=base64.b64decode(base64_image)
    )

    # コンテンツ生成リクエストを送信
    responses = model.generate_content(
        [image1, """この画像について限界まで詳細に説明してください lang ja"""],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    # 生成されたテキストを結合
    generated_text = ""
    for response in responses:
        generated_text += response.text

    return generated_text

# def recognize_video_text_gemini(model, video_path):
#     """
#     Geminiモデルを使用して動画認識を行う関数

#     Args:
#         model (str): 使用するGeminiモデルの名前
#         video_path (str): 動画ファイルのパス

#     Returns:
#         str: 生成されたテキスト
#     """
#     model = initialize_gemini_model(model)

#     # 動画ファイルをBase64エンコード
#     with open(video_path, "rb") as video_file:
#         base64_video = base64.b64encode(video_file.read()).decode('utf-8')

#     # 動画データをPartオブジェクトとして作成
#     video1 = Part.from_data(
#         mime_type="video/mp4",
#         data=base64.b64decode(base64_video)
#     )

#     # コンテンツ生成リクエストを送信
#     responses = model.generate_content(
#         [video1, """この動画について限界まで詳細に説明してください lang ja"""],
#         generation_config=generation_config,
#         safety_settings=safety_settings,
#         stream=True,
#     )

#     # 生成されたテキストを結合
#     generated_text = ""
#     for response in responses:
#         generated_text += response.text

#     return generated_text

# def generate_gemini_response(model, prompt):
#     """
#     Geminiモデルを使用してテキストを生成する関数

#     Returns:
#         str: 生成されたテキスト
#     """
#     model = initialize_gemini_model(model)

#     responses = model.generate_content(
#         [prompt],
#         generation_config=generation_config,
#         safety_settings=safety_settings,
#         stream=True,
#     )

#     generated_text = ""
#     for response in responses:
#         generated_text += response.text

#     return generated_text

# # 共通設定
# generation_config = {
#     "max_output_tokens": 8192,
#     "temperature": 1,
#     "top_p": 0.95,
# }

# safety_settings = {
#     generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
# }

if __name__ == "__main__":
    main()
