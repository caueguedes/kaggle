import fuzzywuzzy
from fuzzywuzzy import process
import chardet
import pandas as pd

professors = pd.read_csv("../input/pakistan-intellectual-capital/pakistan_intellectual_capital.csv")

# Unnamed: | Teacher Name |	University Currently Teaching |	Department | Province |
# University | Located | Designation |	Terminal Degree | Graduated from |
# Country | Year | Area of Specialization/Research Interests| Other Information

print(professors.Country.unique())

professors['Coutry'] = professors['Country'].str.lower()
professors['Coutry'] = professors['Country'].str.strip()

# FUZZY matching
countries = professors['Country'].unique()
countries.sort()

matches = fuzzywuzzy.process.extract(
    'south korea', countries, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

matches


def replace_matches_in_column(df, column, string_to_match, min_ratio=47):
    strings = df[column].unique()
    matches = fuzzywuzzy.process.extract(string_to_match, strings,
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]
    rows_with_matches = df[column].isin(close_matches)
    df.loc[rows_with_matches, column] = string_to_match
    print("All Done")


replace_matches_in_column(df=professors, column='Country', string_to_match="south korea")


