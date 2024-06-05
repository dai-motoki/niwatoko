# クラス: Anthropic解釈系AI
## 共通
```python.Anthropic解釈系AI
import anthropic
client = anthropic.Anthropic()

```

## 関数: テキスト生成AI
```python.Anthropic解釈系AI.解釈系AI
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