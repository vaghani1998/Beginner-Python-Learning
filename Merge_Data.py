# How can merge data to two files
# How to Join Concept in a python pandas library

import pandas as pd

sales = pd.read_csv('Csv_file/salesmen.csv', index_col='Salesman')

Quarter = pd.read_csv('Csv_file/quarters.csv', index_col='Salesman')

# this is a normal example: it is not an equal database
both = pd.concat([sales, Quarter], axis="index")
print(both)

# How-to Join two Datafiles
foods = pd.read_csv('Csv_file/restaurant_foods.csv')

customer = pd.read_csv('Csv_file/restaurant_customers.csv')

merge_l = foods.merge(customer, how='left', on='Food ID')
print(merge_l)

merge_r = customer.merge(foods, how='right', on='Food ID')
print(merge_r)

merge_inner = foods.merge(customer, how='inner', on='Food ID')
print(merge_inner)