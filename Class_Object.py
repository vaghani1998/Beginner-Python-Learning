# Class as a Represent body & bleu print
# Classes are created using class keyword.

class car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


check = car('POLO', 'Volkswagen')

print(check.name)
print(check.brand)


import pandas as pd
# How to series work in list also Dictionary

animal = ['Tiger', 'Monkey', 'Python', 'Crocodile']  # This is List
Number = pd.Series(animal)
print(Number)

data = {"Name": 'Alexa', "Age": 45, "Occupation": 'Engineering', "height": 159,
        'Hobby': ['Cricket', 'HollyBall', 'Football']}                          # This is Dictionary data

check1 = pd.Series(data)
print(check1)

# How to series in_built function of Statistics fun

example = pd.Series([45.78, 11.52, 45, 6.8])
print(example)

Sum = example.sum()
print(Sum)

Avg = example.mean()
print(Avg)

Std = example.std()
print(Std)

# An attribute is a fact, a detail, a characteristics of object

char = pd.Series(['Smart', 'Handsome', 'Brilliant', 'Good looking', 'Humble', 'Charming', 'innocent'])

Size = char.size
print(Size)

Uniq = char.is_unique
print(Uniq)

index = char.index
print(index)

info = char.info
print(info)

typed = char.dtype.type
print(typed)

# Parameter & Arguments
# A parameter is a name for expected input to a function/method/class instantiation.
# an Argument is the concrete value we provide for a parameter during invocation.

country = ['India', 'china', 'US', 'Japan', 'Germany']
code = [91, 93, 1, 92, 49]

print(pd.Series(country))
print(pd.Series(code))

Merge = pd.Series(country, code)
print(Merge)
