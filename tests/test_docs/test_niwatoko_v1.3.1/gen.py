from pathlib import Path
from openai import OpenAI
import requests

# OpenAIクライアントの初期化
client = OpenAI()

# バナー画像の生成
banner_theme = "最新のAI技術を活用した革新的なサービス"
banner_style = "モダンでスタイリッシュなデザイン"
prompt = f"{banner_theme}, {banner_style}"

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
image_response = requests.get(image_url)

# 画像をダウンロードしてpngで保存
image_path = Path(__file__).parent / "generated_banner.png"
with open(image_path, 'wb') as image_file:
    image_file.write(image_response.content)
# 出力結果のファイルパスをprint
print(f"バナー画像が保存されました: {image_path}")

# 音声合成の生成
speech_text = f"こちらは、{banner_theme}をテーマにした{banner_style}のバナー画像です。"
speech_file_path = Path(__file__).parent / "banner_description.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=speech_text
)

response.stream_to_file(speech_file_path)
# 出力結果のファイルパスをprint
print(f"音声ファイルが保存されました: {speech_file_path}")