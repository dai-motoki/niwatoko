# クラス: Anthropic解釈系AI
## 共通
```python.Anthropic認識系AI
import anthropic
client = anthropic.Anthropic()

```

## 関数: 画像認識
```python.Anthropic解釈系AI.画像生成
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "こんにちは"
                }
            ]
        }
    ]
)
print(message.content)

```