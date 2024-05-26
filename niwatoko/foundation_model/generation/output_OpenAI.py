import requests
import os
from pathlib import Path
from openai import OpenAI

# 環境変数からAPIキーを取得
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# 画像生成
response = client.images.generate(
    model="dall-e-3",
    prompt="夏の午後の校舎の風景。青空に大きな入道雲が浮かび、校舎に影を落としている。窓から差し込む日差しが教室の机に反射し、静かな雰囲気を醸し出している。リアルな写真のようなディテールのあるイラスト。光と影のコントラストを強調し、夏の暑さと静けさを表現する。",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
image_response = requests.get(image_url)

# 画像をダウンロードしてpngで保存
media_dir = Path("./media")
media_dir.mkdir(exist_ok=True)
image_path = media_dir / "school_afternoon.png"
with open(image_path, 'wb') as image_file:
    image_file.write(image_response.content)

# 音声合成
speech_file_path = media_dir / "narration.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="夏の午後、青空に大きな入道雲が浮かんでいます。雲の影が校舎に落ち、教室にひんやりとした空気が流れ込んでいます。窓からの日差しが机に反射し、静かな雰囲気が漂っています。"
)

response.stream_to_file(speech_file_path)

# 字幕ファイル作成
subtitle_file_path = media_dir / "narration.srt"
with open(subtitle_file_path, "w") as f:
    f.write(
        """
1
00:00:00,000 --> 00:00:05,000
夏の午後、青空に大きな入道雲が浮かんでいます。

2
00:00:05,000 --> 00:00:10,000
雲の影が校舎に落ち、教室にひんやりとした空気が流れ込んでいます。

3
00:00:10,000 --> 00:00:15,000
窓からの日差しが机に反射し、静かな雰囲気が漂っています。
        """
    )

# 画像ファイルを動画ファイルに変換
os.system(
    f"ffmpeg -loop 1 -i {image_path} -c:v libx264 -t 00:00:15 -pix_fmt yuv420p -vf scale=1024:1024 -r 25 {media_dir / 'school_afternoon.mp4'}"
)

# ビデオファイル生成
os.system(
    f"ffmpeg -i {media_dir / 'school_afternoon.mp4'} -i {speech_file_path} -vf subtitles={subtitle_file_path} -c:v libx264 -c:a aac -map 0:v -map 1:a {media_dir / 'school_afternoon_with_narration.mp4'}"
)
