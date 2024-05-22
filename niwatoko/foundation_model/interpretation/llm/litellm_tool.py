import os
from litellm import completion
import niwatoko 

from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む
niwatoko_dir = os.path.dirname(niwatoko.__file__)                        # zoltraakパッケージのディレクトリパスを取得
with open(f"{niwatoko_dir}/grammar/system.md", "r", encoding = "utf-8") as f:
    system_prompt = f.read()

def generate_response(model, prompt, max_tokens, temperature):
    """
    LiteLLMを使用してプロンプトに対する応答を生成する関数。

    Args:
        prompt (str): 応答を生成するためのプロンプト。

    Returns:
        str: 生成された応答テキスト。
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    response = completion(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature
    )

    return response.choices[0].message.content.strip()