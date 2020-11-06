# module on python to fix text from cells
# https://ftfy.readthedocs.io/en/latest/

import chardet
import pandas as pd

before = "This is the euro symbol: €"
bytes_before = before.encode("utf-8", errors="replace")
print(bytes_before.decode("utf-8"))

# import an non UTF-8 file
kickstarter_2016 = pd.read_csv("../input/kickstarter-projects/ks-projects-201612.csv")
#will raise errors

with open("../input/kickstarter-projects/ks-projects-201612.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))

print(result)
# {'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}


pd.to_csv('file_name_to_be_saved.csv')


police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding='Windows-1252')