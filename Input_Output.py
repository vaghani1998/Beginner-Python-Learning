# How to Input-Output work

import pandas as pd

url = "https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv"

Baby_name = pd.read_csv(url)
Baby_name.head()
print(Baby_name)

json = Baby_name.to_json()
print(json)

# This method can use to csv datasheet generate
csv_data = Baby_name.to_csv('Baby_name.csv')

print(csv_data)


