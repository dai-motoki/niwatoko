import os
from openai import OpenAI
import niwatoko 
from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む
niwatoko_dir = os.path.dirname(niwatoko.__file__)                        # zoltraakパッケージのディレクトリパスを取得
with open(f"{niwatoko_dir}/grammar/system.md", "r", encoding = "utf-8") as f:
    system_prompt = f.read()


api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise openai.OpenAIError("api_keyクライアントオプションは、クライアントにapi_keyを渡すか、OPENAI_API_KEY環境変数を設定することで設定する必要があります。詳細は以下のURLでOpenAI API KEYをセットしてください: https://platform.openai.com/api-keys")

client = OpenAI(
    api_key=api_key
)
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

def generate_response_gpt4o(prompt, max_tokens, temperature):
    """
    OpenAI APIを使用してGPT-4oモデルでプロンプトに対する応答を生成する関数。

    Args:
        prompt (str): 応答を生成するためのプロンプト。
        max_tokens (int): 生成する最大トークン数。
        temperature (float): 生成時のランダム性を制御する温度パラメータ（0から1の範囲）。

    Returns:
        str: 生成された応答テキスト。
    """
    print(prompt)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content.strip()
