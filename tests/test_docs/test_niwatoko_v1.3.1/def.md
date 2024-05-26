# バナー自動生成要件定義書

## 引用
- `GPT生成AI` = [def_gen_gpt_api.md]

```python
## クラス: GPT生成AI
### 共通
from pathlib import Path
from openai import OpenAI
client = OpenAI()
```

### 関数: 画像生成
```python
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

### 関数: 音声合成
```python
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

## TODO
`画像生成`と`音声合成`を使ってバナー画像と説明音声を含めたビジネスアイデアの詳細要件定義書を作成して

- 計画
    - GitHubのツリーを記載して、最後のコミットを展開
    - ディレクトリ構成と詳細を記述（コードブロック内に）
    - シークエンス図を記載
    - オブジェクト指向の図を作成

## 実行言語
- md. 日本語
- 1枚のファイルで

## GitHubツリー構造
```
.
├── README.md
├── def_gen_gpt_api.md
├── src
│   ├── gpt_image_generator.py
│   └── gpt_voice_generator.py
└── assets
    ├── generated_image.png
    └── speech.mp3
```

## ディレクトリ構成詳細
- `README.md`: プロジェクトの概要と使用方法を記載。
- `def_gen_gpt_api.md`: GPT生成AIのAPI定義書。
- `src/`: ソースコードを格納するディレクトリ。
  - `gpt_image_generator.py`: 画像生成を行うスクリプト。
  - `gpt_voice_generator.py`: 音声合成を行うスクリプト。
- `assets/`: 生成された画像や音声ファイルを格納するディレクトリ。
  - `generated_image.png`: 生成されたバナー画像。
  - `speech.mp3`: 生成された説明音声。

## シークエンス図
```plaintext
ユーザー -> GPT生成AI: 画像生成リクエスト
GPT生成AI -> OpenAI API: 画像生成要求
OpenAI API -> GPT生成AI: 画像URLを返す
GPT生成AI -> 画像URL: 画像をダウンロード
GPT生成AI -> ファイルシステム: 画像を保存
GPT生成AI -> ユーザー: 画像生成完了通知

ユーザー -> GPT生成AI: 音声合成リクエスト
GPT生成AI -> OpenAI API: 音声合成要求
OpenAI API -> GPT生成AI: 音声データを返す
GPT生成AI -> ファイルシステム: 音声を保存
GPT生成AI -> ユーザー: 音声合成完了通知
```

## オブジェクト指向図

```plaintext
+--------------------+
|     GPT生成AI      |
+--------------------+
| - client: OpenAI   |
+--------------------+
| + 画像生成()       |
| + 音声合成()       |
+--------------------+

+--------------------+
|    OpenAI API      |
+--------------------+
| + images.generate()|
| + audio.speech.create()|
+--------------------+
```