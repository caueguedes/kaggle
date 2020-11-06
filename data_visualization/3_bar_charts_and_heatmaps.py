import pandas as pd
import matplotlib as plt
import seaborn as sns

flight_filepath = "../input/flight_delays.csv"
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# Bar
plt.figure(figsize=(10,6))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

sns.barplot(x=flight_data.index, y=flight_data['NK'])
plt.ylabel("Arrival delay (in minutes)")


plt.figure(figsize=(14,7))
plt.figure(figsize=(14,7))
sns.heatmap(data=flight_data, annot=True)
plt.xlabel("Airline")
