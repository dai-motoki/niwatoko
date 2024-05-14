import pandas as pd
import matplotlib.pyplot as plt

# Load data
zoltraak = pd.read_csv('./zoltraak2.csv')
niwatoko = pd.read_csv('./niwatoko2.csv')

# Convert 'download_date' to datetime
zoltraak['download_date'] = pd.to_datetime(zoltraak['download_date'])
niwatoko['download_date'] = pd.to_datetime(niwatoko['download_date'])

# Merge data
merged_data = pd.merge(zoltraak, niwatoko, on='download_date', how='outer', suffixes=('_zoltraak', '_niwatoko'))

# Fill NaN values with 0
merged_data = merged_data.fillna(0)

# Sum cumulative downloads
merged_data['cumulative_downloads'] = merged_data['cumulative_downloads_zoltraak'] + merged_data['cumulative_downloads_niwatoko']

# Sort by date
merged_data = merged_data.sort_values('download_date')

# Plot
plt.figure(figsize=(10, 6))
plt.plot(merged_data['download_date'], merged_data['cumulative_downloads'], label='Total Cumulative Downloads')
plt.xlabel('Date')
plt.ylabel('Cumulative Downloads')
plt.title('Cumulative Downloads Over Time')
plt.legend()
plt.grid(True)
plt.show()