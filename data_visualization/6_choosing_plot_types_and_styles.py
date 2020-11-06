# Styling plots
sns.set_style("dark")

# Line chart
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

# "darkgrid", (2)"whitegrid", (3)"dark", (4)"white", and (5)"ticks"