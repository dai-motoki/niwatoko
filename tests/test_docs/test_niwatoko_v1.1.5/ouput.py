import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み
zoltraak_df = pd.read_csv('zoltraak2.csv')
niwatoko_df = pd.read_csv('niwatoko2.csv')

# download_date列を日付型に変換
zoltraak_df['download_date'] = pd.to_datetime(zoltraak_df['download_date'])
niwatoko_df['download_date'] = pd.to_datetime(niwatoko_df['download_date'])

# データフレームをマージ
merged_df = pd.concat([zoltraak_df, niwatoko_df])

# 日付が重複する行の累積ダウンロード数を合計
merged_df = merged_df.groupby('download_date').sum().reset_index()

# 累積ダウンロード数の推移を折れ線グラフで描画
plt.figure(figsize=(10,5))
plt.plot(merged_df['download_date'], merged_df['cumulative_downloads'], marker='o')
plt.title('Cumulative Downloads Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Downloads')
plt.grid(True)
plt.show()