import pandas as pd
import numpy as np

nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")
nfl_data.head()

missing_values_count = nfl_data.isnull().sum()
missing_values_count
missing_values_count[0:10]

# how many total missing values do we have?
total_cells = np.product(nfl_data.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
nfl_data.dropna()

# Drop
columns_with_na_dropped = nfl_data.dropna(axis=1)
columns_with_na_dropped.head()

# Fill
subset_nfl_data = nfl_data.loc[:, 'EPA':'Season'].head()
