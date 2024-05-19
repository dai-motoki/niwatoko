import pandas as pd
import matplotlib.pyplot as plt

# 'zoltraak.csv'の読み込み
zoltraak = pd.read_csv('./zoltraak2.csv')
zoltraak['download_date'] = pd.to_datetime(zoltraak['download_date'])
zoltraak = zoltraak.set_index('download_date')

# 'niwatoko.csv'の読み込み
niwatoko = pd.read_csv('./niwatoko2.csv')
niwatoko['download_date'] = pd.to_datetime(niwatoko['download_date'])
niwatoko = niwatoko.set_index('download_date')

# データフレームの結合
df = pd.concat([zoltraak, niwatoko], axis=1)
df = df.fillna(0)
df['total_downloads'] = df['cumulative_downloads_x'] + df['cumulative_downloads_y']

# 折れ線グラフの描画
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['total_downloads'])
plt.xlabel('Date')
plt.ylabel('Cumulative Downloads')
plt.title('Cumulative Downloads Trend')
plt.grid()
plt.show()