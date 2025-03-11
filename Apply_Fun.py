# How to apply function work in Series model
# Also Mep (map()) method will do it

import pandas as pd

pokemon = pd.read_csv('Csv_file/pokemon.csv', usecols=['Name']).squeeze('columns')

print(pokemon)

Apply = pokemon.apply(len)

print(Apply)


# which onw method to lets do it

def count_of_no(poke):
    return poke.count('d')


let = pokemon.apply(count_of_no)

print('check', let)

print('---------- Map ----------')
# Let's try to Mep function (Method)
# Create simple dictionary python

pokemon = pd.read_csv('Csv_file/pokemon.csv', index_col='Name').squeeze('columns')

dic = {
    "Grass, Poison": 45,
    "Neuclear, Power": 15,
    "Fire, Flying": 12,
    "Megnet, Stick": 81,
    "Water, Dragon": 50
}

# Try with Series Model
dic1 = pd.Series({
    "Grass, Poison": 45,
    "Neuclear, Power": 15,
    "Fire, Flying": 12,
    "Megnet, Stick": 81,
    "Water, Dragon": 50
})
print(dic1)

Map = pokemon.head(10).map(dic)  # This Mep fun use with another Series data try to match label and add values first
# list.
print(Map)
