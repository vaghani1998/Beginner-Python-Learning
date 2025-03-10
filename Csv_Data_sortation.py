# The 'sort index' method use to Sort data in Ascending or Descending order
# More over head and tail using first and last data show:

import pandas as pd

data = pd.read_csv('Csv_file/foods.csv')

print(data)

check = data.head(5)

print(check)

check1 = data.tail(5)

print(check1)

# How to check null data

Null = data.isnull().sum()

print(Null)

# How to particular column show first position

colFirst = data.set_index('Gender', drop=False)

print(colFirst)

just_Col = pd.read_csv('Csv_file/google_stock_price.csv', index_col='Price')

print(just_Col)

a1 = just_Col.squeeze('columns')

print(a1)

# How to sort index

Sort = just_Col.sort_index(ascending=False)

print(Sort)

# How to Particulate index location Show:

Pokemon = pd.read_csv('Csv_file/pokemon.csv', usecols=['Name']).squeeze('columns')

i_loc = Pokemon.iloc[50]

print('Index No 50:', i_loc)

list_loc = Pokemon.iloc[[45, 55, 66, 77]]

desc = list_loc.sort_index(ascending=False)

print(list_loc)
print(desc)  # Order following

to_loc = Pokemon.iloc[10:50].sort_index(ascending=False)

print(to_loc)  # Start to End point values show

last = Pokemon.iloc[-9:-1]
print('this is location:', last)

# How to index label show to series model:

foods = pd.read_csv('Csv_file/foods.csv', index_col='First Name').squeeze('columns')

print(foods)

label = foods.loc['Anna']

print(label)

# More than label show

All = foods.loc[['Anna', 'Deborah']]

print(All)

series = pd.read_csv('Csv_file/foods.csv', index_col='First Name', header=0)
loc = series.loc['Anna']
print(loc)

