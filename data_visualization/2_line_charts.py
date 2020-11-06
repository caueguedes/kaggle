import pandas as pd
import matplotlib as plt
import seaborn as sns

spotify_filepath = "../input/spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

spotify_data.head()  # .tail()

plt.figure(figsize=(14, 6))
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

sns.lineplot(spotify_data)


sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
plt.xlabel("Date")
