import os

translation_target_languages = [
    "FR",
    "DE", 
    "EN",
    "ES",
    "IT",
    "PT",
    "RU",
    "ZH",
    "KO",
    "AR"
]

japanese_file = "README_ja.md"

for target_lang, target_lang_code in zip(["フランス語", "ドイツ語", "英語", "スペイン語", "イタリア語", "ポルトガル語", "ロシア語", "中国語", "韓国語", "アラビア語"], translation_target_languages):
    translation_file = f"translation_{target_lang_code}.md"
    with open(translation_file, "w", encoding="utf-8") as f:
        f.write(f"{target_lang}への翻訳:\n\n")
        with open(japanese_file, "r", encoding="utf-8") as ja_file:
            for line in ja_file:
                # ここで各行を target_lang に翻訳する処理を行う
                translated_line = line  # 仮置き
                f.write(translated_line)
    
    os.system(f"niwatoko {translation_file} -o README_{target_lang_code}.md")