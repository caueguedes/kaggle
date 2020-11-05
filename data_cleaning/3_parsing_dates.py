import pandas as pd
# https://www.kaggle.com/residentmario/time-series-plotting-optional


landslides = pd.DataFrame({'date': ['3/2/07', '3/22/07', '4/6/07']})
landslides.head()

landslides['date'].head(1)  # 1/17/07
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")
# landslides['date_parsed'] = pd.to_datetime(landslides['Date'], infer_datetime_format=True)

day_of_month_landslides = landslides['date_parsed'].dt.day
day_of_month_landslides.head()


