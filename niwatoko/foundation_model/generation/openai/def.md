# クラス: OpenAI生成系AI

## 共通
```python.OpenAI生成AI
from pathlib import Path
from openai import OpenAI
client = OpenAI()
```

## 関数: 画像生成
```python.OpenAI生成系AI.画像生成
response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

import requests
from pathlib import Path

image_url = response.data[0].url
image_response = requests.get(image_url)

# 画像をダウンロードしてpngで保存
image_path = Path(__file__).parent / "generated_image.png"
with open(image_path, 'wb') as image_file:
    image_file.write(image_response.content)
# 出力結果のファイルパスをprint
print(f"画像が保存されました: {image_path}")

```

## 関数: 音声合成
```python.OpenAI生成系AI.音声合成
speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
# 出力結果のファイルパスをprint
print(f"音声ファイルが保存されました: {speech_file_path}")
```

