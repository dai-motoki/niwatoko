import os
from pathlib import Path
from openai import OpenAI
import requests

# OpenAI APIクライアントの初期化
client = OpenAI()

# 画像生成
image_prompt = "a peaceful afternoon at a school campus, with students walking around and enjoying the warm sunlight"
image_response = client.images.generate(
    model="dall-e-3",
    prompt=image_prompt,
    size="1024x1024",
    quality="standard",
    n=1
)
image_url = image_response.data[0].url
image_path = Path("media") / "school_afternoon_image.png"
os.makedirs(image_path.parent, exist_ok=True)
with open(image_path, 'wb') as f:
    f.write(requests.get(image_url).content)
print(f"Image saved to: {image_path}")

# 音声合成
speech_text = "It was a peaceful afternoon at the school campus. Students were walking around, enjoying the warm sunlight and the gentle breeze. Some were chatting with friends, while others were studying or reading under the shade of the trees. The campus felt alive with the energy of young minds exploring and discovering the world around them."
speech_response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=speech_text
)
speech_path = Path("media") / "school_afternoon_story.mp3"
os.makedirs(speech_path.parent, exist_ok=True)
speech_response.stream_to_file(speech_path)
print(f"Audio saved to: {speech_path}")
