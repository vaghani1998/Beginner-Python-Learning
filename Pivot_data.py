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

# How-to Group by received dataset

grouped = pivot.groupby(by=['Salesman'], observed=True)['Revenue'].sum()
print(grouped)

# How-to get-group by each sector values show:

fortune = pd.read_csv('Csv_file/fortune1000.csv', index_col='Rank')
print('check', fortune)
fortune.info()

sector = fortune.groupby('Sector')
length = len(sector)
size = sector.size()
print(length)
print(size)

get_group = sector.get_group('Financials').sort_index()
print(get_group)

# Now we can observation all sectors' revenue:
# Step of 1st Create Group then it group calculation with revenue filed.

total_sector = sector['Revenue'].sum()
print(total_sector)  # this is a Direct method

total_sector1 = fortune[fortune['Sector'] == 'Business Services']['Revenue'].sum()
print('Revenue of Business Services:', total_sector1)  # this is an indirect method

# Check how much employee work in sector by:

total_emp = sector['Employees'].sum()
print(total_emp)

two_col = sector[['Revenue', 'Profits']].sum()
print(two_col)

# How-to aggregate function work:

sector_agg = sector.agg({'Profits': 'max', 'Revenue': 'min', 'Employees': 'mean'})
print(sector_agg)
