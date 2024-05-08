import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 1. データの読み込み
df = pd.read_csv('data.csv')
df['download_date'] = pd.to_datetime(df['download_date'])

# 2. 欠損値の処理
df = df.fillna(0)

# 3. 累積値の計算
df['cumulative_total'] = df['zoltraak'] + df['niwatoko']

# 4. 日本語フォントの設定
font_path = 'path/to/your/japanese/font.ttf'
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# 5. グラフの作成
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['download_date'], df['cumulative_total'])
ax.set_title('累積値の推移', fontproperties=font_prop)
ax.set_xlabel('日付', fontproperties=font_prop)
ax.set_ylabel('累積値', fontproperties=font_prop)
ax.legend(['累積値'], prop=font_prop)
ax.xaxis.set_tick_params(rotation=45)
ax.grid(True)

# 6. グラフの表示
plt.show()