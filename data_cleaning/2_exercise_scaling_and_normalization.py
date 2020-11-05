import pandas as pd

original_data = pd.DataFrame(kickstarters_2017.usd_goal_real)

# Scaling ################
from mlxtend.preprocessing import minmax_scaling

scaled_data = minmax_scaling(original_data, columns=['usd_goal_real'])

# Normalization
from scipy import stats
index_of_positive_pledges = original_data.usd_pledged_real > 0
positive_pledges = original_data.usd_pledged_real.loc[index_of_positive_pledges]

normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0],
                               name='usd_pledged_real', index=positive_pledges.index)