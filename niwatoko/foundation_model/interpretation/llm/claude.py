import os
import anthropic
import niwatoko 

from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む
niwatoko_dir = os.path.dirname(niwatoko.__file__)                        # zoltraakパッケージのディレクトリパスを取得
with open(f"{niwatoko_dir}/grammar/system.md", "r", encoding = "utf-8") as f:
    system_prompt = f.read()

def generate_response(model, prompt, max_tokens, temperature):
    """
    Anthropic APIを使用してプロンプトに対する応答を生成する関数。

    Args:
        prompt (str): 応答を生成するためのプロンプト。

    Returns:
        str: 生成された応答テキスト。
    """
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")  # 環境変数からAPI keyを取得
    )
    # print(prompt)


    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [

                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    # print(response)
    
    return response.content[0].text.strip()
