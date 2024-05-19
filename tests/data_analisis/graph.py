import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties
import pandas as pd

# データの読み込み
df_zoltraak = pd.read_csv('../test_docs/test_niwatoko_v1.1.5/zoltraak3.csv')
df_niwatoko = pd.read_csv('../test_docs/test_niwatoko_v1.1.5/niwatoko3.csv')

# 日付列を datetime 型に変換
df_zoltraak['download_date'] = pd.to_datetime(df_zoltraak['download_date'])
df_niwatoko['download_date'] = pd.to_datetime(df_niwatoko['download_date'])

# 2つのデータフレームを結合
df = pd.merge(df_zoltraak, df_niwatoko, on='download_date', how='outer')
df = df.rename(columns={'cumulative_downloads_x': 'zoltraak', 'cumulative_downloads_y': 'niwatoko'})
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

# グラフの中央にダウンロード数を表示
total_downloads = df["cumulative_total"].iloc[-1]
release_days = (df["download_date"].iloc[-1] - df["download_date"].iloc[0]).days + 1
plt.text(0.5, 0.7, f'総ダウンロード回数', fontsize=48, fontweight='bold', 
         ha='center', va='center', transform=plt.gca().transAxes, fontproperties=jp_font_prop)
plt.text(0.5, 0.5, f'{total_downloads/10000:.2f}万', fontsize=72, fontweight='bold',
         ha='center', va='center', transform=plt.gca().transAxes, fontproperties=jp_font_prop)
plt.text(0.5, 0.3, f'リリースから{release_days}日', fontsize=36, fontweight='bold', 
         ha='center', va='center', transform=plt.gca().transAxes, fontproperties=jp_font_prop)

# 軸ラベルとタイトルの設定 
# plt.title(f'総合ダウンロードデータ: {total_downloads/10000:.2f}万', fontsize=48, fontweight='bold', fontproperties=jp_font_prop)
# plt.xlabel('日付', fontsize=30, fontweight='bold', fontproperties=jp_font_prop)
plt.ylabel('ダウンロード数', fontsize=30, fontweight='normal', fontproperties=jp_font_prop)

# X軸とY軸の目盛りを日付に設定し、フォントサイズを大きくする
plt.xticks(df['download_date'], df['download_date'].dt.strftime('%Y-%m-%d'), rotation=45, fontsize=18, fontproperties=jp_font_prop)
plt.yticks(fontsize=18)

# グリッドの表示
plt.grid(True)
# 表示
plt.show()


# 上記を詳細要件定義書として1行1行日本語でマークダウン形式で出力して
# 日本語のみでok、行間空けない、ファイルパスは正確に
# みやすくマークダウンで記載して、断定口調で(要件定義書です）プログラムは消す。
# ファイルパスはのこす