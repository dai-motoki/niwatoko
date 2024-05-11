import pandas as pd
import matplotlib.pyplot as plt

# 'zoltraak' データの読み込み
zoltraak = pd.read_csv('./zoltraak.csv')

# 'niwatoko' データの読み込み
niwatoko = pd.read_csv('./niwatoko.csv')

# 2つのデータフレームを結合
df = pd.concat([zoltraak, niwatoko])

# 日付をインデックスに設定
df['download_date'] = pd.to_datetime(df['download_date'])
df = df.set_index('download_date')

# 日付が重複する行の合計値を計算
df = df.groupby(df.index).sum()

# 折れ線グラフの描画
plt.figure(figsize=(12, 6))
plt.plot(df['cumulative_downloads'], color='#4169E1')
plt.title('Cumulative Downloads')
plt.xlabel('Date')
plt.ylabel('Cumulative Downloads')
plt.grid()
plt.show()


# 上記を要件定義書にして
# マークダウン形式で