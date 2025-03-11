# How to use Mathematics function work:

import pandas as pd

stock = pd.read_csv('Csv_file/google_stock_price.csv', usecols=['Price']).squeeze('columns')
print(stock)

# Sum function
Sum = stock.head().sum()
print('Sum of 5 records:', Sum)

# Count function
Count = stock.head().count()
print('Count of 5 records:', Count)

# Product function
pro = pd.Series([1,5,6,7])
Product = pro.product()
print('Product of list:', Product)

# Mean function
Mean = stock.head().mean()
print('Mean of 5 records:', Mean)

# Standers Deviation function
Std = stock.head().std()
print('Std of 5 records:', Std)

# Max function
Max = stock.head().max()
print('Max of 5 records:', Max)

# Min function
Min = stock.head().min()
print('Min of 5 records:', Min)

# Median function
Median = stock.head().median()
print('Median of 5 records:', Median)

# Mode function
Mode = stock.head().mode()
print('Mode of 5 records:', Mode)

print('--*$@ Describe of all function @$*--')

# Describe function
Des = stock.describe()
print(Des)

# In this part Mathematics Operation

# Addition function
add = stock.head().add(10)
Addi = stock.head(1) + 10
print('Addition Values:         ', add)
print('Alternative Add Option   ', Addi)

# Subtraction function
sub = stock.head().sub(10)
Subtr = stock.head(1) - 10
print('Subtraction Values:      ', sub)
print('Alternative Sub Option   ', Subtr)

# Multiplication function
mul = stock.head().mul(5)
Multi = stock.head(1) * 5
print('Multiplication Values:   ', mul)
print('Alternative Multi Option ', Multi)

# Division function
div = stock.head().div(5)
Division = stock.head(1) / 5
print('Division Values:         ', div)
print('Alternative Divi Option  ', Division)

# The Values_count method use to the return number each time the unique values show.

pokemon = pd.read_csv('Csv_file/pokemon.csv', index_col='Name').squeeze('columns')

print(pokemon)

count = pokemon.value_counts()
print(count)

print('--------------------------')

check = pokemon.value_counts(normalize=True) * 100
print(check)

print('--------------------------')

ascending = pokemon.value_counts(ascending=True)
print(ascending)
