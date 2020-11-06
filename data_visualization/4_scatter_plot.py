import pandas as pd
import matplotlib as plt
import seaborn as sns

insurance_filepath = "../input/insurance.csv"
insurance_data = pd.read_csv(insurance_filepath)

insurance_data.head()
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# Regression line shows the strength of the relation between bmi an high charges due to elevated health risks
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# Colored
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoke'])

sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)


#  Categorical Scatter plot
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])
