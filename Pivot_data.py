# How can covert in to Pivot table:

import pandas as pd

pivot = pd.read_csv('Csv_file/salesmen.csv')

# pivot['Date'] = pd.to_datetime(pivot['Date'], format='%m/%d/%Y')
pivot['Salesman'] = pivot['Salesman'].astype('category')
pivot.info()
print(pivot)

# this difference between tall data set to short data set
convert = pivot.pivot(index='Date', columns='Salesman', values='Revenue')
print(convert)

