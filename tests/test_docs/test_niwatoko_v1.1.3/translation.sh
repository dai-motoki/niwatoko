# 日本語ファイルを各言語に翻訳するスクリプトを生成します。

# フランス語に翻訳
sed 's/{{Lang}}/FR/g' translation.md > README_fr.md
niwatoko README_fr.md -o README_fr.md

# ドイツ語に翻訳
sed 's/{{Lang}}/DE/g' translation.md > README_de.md
niwatoko README_de.md -o README_de.md

# 英語に翻訳
sed 's/{{Lang}}/EN/g' translation.md > README_en.md
niwatoko README_en.md -o README_en.md

# スペイン語に翻訳
sed 's/{{Lang}}/ES/g' translation.md > README_es.md
niwatoko README_es.md -o README_es.md

# イタリア語に翻訳
sed 's/{{Lang}}/IT/g' translation.md > README_it.md
niwatoko README_it.md -o README_it.md

# ポルトガル語に翻訳
sed 's/{{Lang}}/PT/g' translation.md > README_pt.md
niwatoko README_pt.md -o README_pt.md

# ロシア語に翻訳
sed 's/{{Lang}}/RU/g' translation.md > README_ru.md
niwatoko README_ru.md -o README_ru.md

# 中国語に翻訳
sed 's/{{Lang}}/ZH/g' translation.md > README_zh.md
niwatoko README_zh.md -o README_zh.md

# 韓国語に翻訳
sed 's/{{Lang}}/KO/g' translation.md > README_ko.md
niwatoko README_ko.md -o README_ko.md

# アラビア語に翻訳
sed 's/{{Lang}}/AR/g' translation.md > README_ar.md
niwatoko README_ar.md -o README_ar.md




