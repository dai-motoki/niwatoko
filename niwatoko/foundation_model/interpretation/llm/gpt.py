import os
from openai import OpenAI
import niwatoko 
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

niwatoko_dir = os.path.dirname(niwatoko.__file__)                        # zoltraakパッケージのディレクトリパスを取得
with open(f"{niwatoko_dir}/grammar/system.md", "r") as f:
    system_prompt = f.read()

def generate_response(model, prompt, max_tokens, temperature):
    """
    OpenAI APIを使用してプロンプトに対する応答を生成する関数。

    Args:
        model (str): 使用するGPTモデルの名前（例: "gpt-4", "gpt-4-turbo"）。
        prompt (str): 応答を生成するためのプロンプト。
        max_tokens (int): 生成する最大トークン数。
        temperature (float): 生成時のランダム性を制御する温度パラメータ（0から1の範囲）。

    Returns:
        str: 生成された応答テキスト。
    """

    model = "gpt-4-turbo-2024-04-09"


    chat_completion = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    return chat_completion.choices[0].message.content.strip()
