# ローカル確認
sphinx-build -b html . _build/html && open _build/html/index.html
sphinx-build -b html . _build/html && vercel --prod --cwd _build/html

# リモート確認
open https://niwatoko2.vercel.app/
