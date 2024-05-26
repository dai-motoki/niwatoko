## クラス: Gemini認識系AI
### 共通
```python.Gemini認識系AI
import Gemini
import base64
import httpx
client = Gemini.Gemini()

```

### 関数: 画像認識
```python.Gemini生成系AI.画像生成

image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image1_media_type = "image/jpeg"
image1_data = base64.b64encode(httpx.get(image1_url).content).decode("utf-8")

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "この画像を説明してください。"
                }
            ],
        }
    ],
)
print(message)

```
