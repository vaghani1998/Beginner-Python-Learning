# The get() method returns the value of the item with the specified key
import pandas as pd

show = pd.read_csv('Csv_file/pokemon.csv', index_col='Name').squeeze('columns')

print(show)

Get = show.get("Metapod")

print(Get)

# More than data show:

Get = show.get(['Kakuna', 'Pidgey'])

print(Get)

Get = show.get(['Kakuna', 'pokion'], 'this last values did not in list')

print(Get)  # In the list not available data ignore.

# How to Override Series values

data = pd.read_csv('Csv_file/foods.csv', usecols=['Item']).squeeze('columns')

print(data)

play = data.iloc[[2, 3, 4]]
print(play)

all = data.head()
print('How head work', all)

play = data.iloc[[2, 3, 4]] = ['Sushi', 'Ice Cream', 'Chalupa']
print(play)

data = pd.read_csv('Csv_file/foods.csv', index_col='Item').squeeze('columns')

print(data)

play = data.loc['Sushi']
print(play)

# How to copy method work with ex.

    #     /\
    #    /  \
    #   /    \
    #  /------\
    # /        \
    # |        |
    # |        |
    # |__|  |__|

#     /\
#    /  \
#   /    \
#  /------\
# /        \
# |        |
# |   -----|-->
# |__|  |__|        # but this home also copy and make different looks.

Copy = pd.read_csv('Csv_file/pokemon.csv', usecols=['Name'])

print(Copy)

now = Copy.squeeze('columns').copy()

print(now)

index = now[0]
p1 = now[0] = 'Something else'
print(p1)
print(index)

last = Copy.head(5)
print('''This time as it's data''', last)

# This same concept copy method use:
then = Copy.squeeze('columns')

print(then)

index = then[0]
p1 = then[0] = 'Something else'
print(p1)
print(index)

# this task help to how to position values add & change:
last = Copy.head(5)
print('This time data change in position', last)

# Output is:
# Name
# 0       Bulbasaur
# 1         Ivysaur
# 2        Venusaur
# 3  Something else
# 4      Charmeleon


