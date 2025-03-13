# The 'sort index' method uses to Sort data in Ascending or Descending order
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

# How to index label show to a series model:

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

# How to check NaN data in Datafile & DataFrame
print('-------- NBA ---------')
nba = pd.read_csv('Csv_file/nba.csv').squeeze('columns')
print(nba)

column = nba.columns
print(column)

row = nba.axes
print(row)

info = nba.info()
print('----------------------- information of data -------------------------')
print('same as', info)

print('------------- columns check simple')

nba = pd.read_csv('Csv_file/nba.csv')

col1 = nba.Team
print(col1)

check = nba[['Team', 'Name', "Position"]]
print(check)

# let's try to play with label

name = nba['Name'].copy()  # copy() method do it parent data set
print(name)

a1 = name.iloc[0] = 'Hello World!'
a2 = name.head()
print(name)
print(a2)

# How to add columns and values in Series
# simple way to

simple = nba["Sports"] = 'Cricket'

print(nba)

multi = nba['Salary'] * 2
multi_or = nba['Salary'].mul(2)

Multi = nba['Salary_Double'] = multi_or
print(nba)

# Subtraction does it
sub = nba['Weight'].sub(-4)

Sub = nba["Weight_Loss"] = sub
print(nba)

# How to Values_count() Method work
a_count = nba['Team'].value_counts()
print(a_count)

# Now Average of Salary by
avg = nba['Salary'].value_counts(normalize=True) * 100
print(avg)

# Sort_Values() Method how to work:
print('-------- Sort_Values ----------')

sorting = nba.sort_values(by='Name', ascending=False)
sorting.head(15)
print(sorting)

# How-to nun Values position

pos = nba.sort_values(by='Salary_Double', na_position='first')
print(pos)

# if I short two columns results

two = nba.sort_values(by=['Name', 'Team'], ascending=[True, False])
print(two)

Another = nba.sort_values(['Salary_Double', 'Weight_Loss'])
print(Another)

# How-to the sort data by index

nba.sort_index()
print(nba)

index_D = nba.sort_index(ascending=False)
print(index_D)