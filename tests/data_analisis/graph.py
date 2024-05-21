import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties
import pandas as pd

# データの読み込み
df_zoltraak = pd.read_csv('../test_docs/test_niwatoko_v1.1.5/zoltraak5.csv')
df_niwatoko = pd.read_csv('../test_docs/test_niwatoko_v1.1.5/niwatoko5.csv')

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

# 最終日のデータを除外
df = df.iloc[:-1]

# 日本語フォントの設定
jp_font_path = '/Users/motokidaisuke/zoltraak/generated/niwatokoのpythonパッケージ_v22/tests/data_analisis/Noto_Sans_JP,Noto_Serif_JP/Noto_Sans_JP/static/NotoSansJP-Bold.ttf'
jp_font_prop = FontProperties(fname=jp_font_path)

# グラフの作成
plt.figure(figsize=(16, 9), facecolor='#f5f5f5')
# グラフの線を青緑色でおしゃれにし、改行して見やすくする
plt.plot(
    df['download_date'], 
    df['cumulative_total'], 
    label='総ダウンロード数 (Zoltraak + Niwatoko)', 
    color='#20B2AA',  # 青緑色
    marker='o', 
    markersize=17, 
    linestyle='-', 
    linewidth=10
)
plt.legend(prop=jp_font_prop, loc='upper left', fontsize=20)

# グラフの中央にダウンロード数を表示
# 総ダウンロード数とリリース日数を計算
total_downloads = df["cumulative_total"].iloc[-1]
release_days = (df["download_date"].iloc[-1] - df["download_date"].iloc[0]).days + 1

# グラフの中央にダウンロード数を表示
plt.text(0.5, 0.65, '総ダウンロード回数', fontsize=48, fontweight='bold', 
         ha='center', va='center', transform=plt.gca().transAxes, fontproperties=jp_font_prop, color='#333333')
plt.text(0.5, 0.4, f'{total_downloads/10000:.2f}万', fontsize=72, fontweight='bold',
         ha='center', va='center', transform=plt.gca().transAxes, fontproperties=jp_font_prop, color='#FF4500')  # 赤色に変更
plt.text(0.5, 0.2, f'リリースから{release_days}日', fontsize=36, fontweight='bold', 
         ha='center', va='center', transform=plt.gca().transAxes, fontproperties=jp_font_prop, color='#333333')
# plt.title(f'総合ダウンロードデータ: {total_downloads/10000:.2f}万', fontsize=48, fontweight='bold', fontproperties=jp_font_prop, color='#FF4500')  # 赤色に変更
# plt.xlabel('日付', fontsize=30, fontweight='bold', fontproperties=jp_font_prop, color='#333333')
plt.ylabel('ダウンロード数', fontsize=30, fontweight='normal', fontproperties=jp_font_prop, color='#333333')

# X軸とY軸の目盛りを日付に設定し、フォントサイズを大きくする
plt.xticks(df['download_date'], df['download_date'].dt.strftime('%Y-%m-%d'), rotation=45, fontsize=18, fontproperties=jp_font_prop, color='#333333')
plt.yticks(fontsize=18, color='#333333')

# グリッドの表示
plt.grid(True, linestyle='--', linewidth=0.5, color='#999999', alpha=0.7)

# PNGファイルとして保存
import datetime
today = datetime.date.today().strftime('%Y-%m-%d')
file_name = f'cumulative_downloads_{today}.png'
plt.savefig(file_name)
print(f'ファイルが保存されました: {file_name}')
