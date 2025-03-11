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


