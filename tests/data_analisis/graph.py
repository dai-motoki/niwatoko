import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties
import pandas as pd

# データの読み込み
data = {
    'download_date': ['2024-04-23', '2024-04-24', '2024-04-25', '2024-04-26', '2024-04-27', '2024-04-28', '2024-04-29', '2024-04-30', '2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04', '2024-05-05', '2024-05-06', '2024-05-07', '2024-05-08', '2024-05-09', '2024-05-10'],
    'zoltraak': [80, 2716, 3232, 4575, 5115, 5523, 5920, 6113, 6421, 7139, 7300, 7520, 7683, 7784, 7998, 8621, 8793, 8824],
    'niwatoko': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1776, 2120, 2274, 2412]
}
df = pd.DataFrame(data)

# 日付をdatetimeに変換
df['download_date'] = pd.to_datetime(df['download_date'])

# 欠損値を0で埋める
df = df.fillna(0)

# 累積値を計算
df['cumulative_total'] = df['zoltraak'] + df['niwatoko']

# 日本語フォントの設定
jp_font_path = '/Users/motokidaisuke/zoltraak/generated/niwatokoのpythonパッケージ_v22/tests/data_analisis/Noto_Sans_JP,Noto_Serif_JP/Noto_Sans_JP/static/NotoSansJP-Bold.ttf'
jp_font_prop = FontProperties(fname=jp_font_path)

# グラフの作成
plt.figure(figsize=(14, 8))
plt.plot(df['download_date'], df['cumulative_total'], label='総ダウンロード数 (Zoltraak + Niwatoko)', color='#FF6347', marker='o', linestyle='-', linewidth=3)
plt.legend(prop=jp_font_prop)

# 軸ラベルとタイトルの設定
plt.title('総合ダウンロードデータ', fontsize=20, fontweight='bold', fontproperties=jp_font_prop)
plt.xlabel('日付', fontsize=18, fontweight='bold', fontproperties=jp_font_prop)
plt.ylabel('ダウンロード数', fontsize=18, fontweight='bold', fontproperties=jp_font_prop)

# X軸の目盛りを日付に設定
plt.xticks(df['download_date'], df['download_date'].dt.strftime('%Y-%m-%d'), rotation=45, fontproperties=jp_font_prop)

# グリッドの表示
plt.grid(True)

# 表示
plt.show()


# 上記を詳細要件定義書として1行1行日本語でマークダウン形式で出力して
# 日本語のみでok、行間空けない、ファイルパスは正確に
# みやすくマークダウンで記載して、断定口調で(要件定義書です）プログラムは消す。
# ファイルパスはのこす