# How can covert in to Pivot table:

import pandas as pd

pivot = pd.read_csv('Csv_file/salesmen.csv')

pivot['Date'] = pd.to_datetime(pivot['Date'], format='%m/%d/%Y')
pivot['Salesman'] = pivot['Salesman'].astype('category')
pivot.info()
print(pivot)

total = pivot.pivot_table(values='Revenue', index='Date').sort_index()
print('check table formate', total)

Sum = pivot.pivot_table(values='Revenue', index=['Salesman', 'Date'], aggfunc='sum', observed=False)
print('Sum of revenues:', Sum)

mean = pivot.pivot_table(values='Revenue', index=['Salesman', 'Date'], aggfunc='mean', observed=False)
print('Mean of revenues:', mean)

# this difference between tall data set to short data set
convert = pivot.pivot(index='Date', columns='Salesman', values='Revenue')
print(convert)

# How can melt method is the inverse of the pivot method.
# New csv dataset file adds name is Quarters Data.

quarters = pd.read_csv('Csv_file/quarters.csv')

quarters.info()
print(quarters)

quarter = quarters.melt(id_vars='Salesman')
print(quarter)




