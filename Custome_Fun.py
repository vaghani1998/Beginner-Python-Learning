# Declaration a function that accepts a values return type
# With Parameter show values

def simple(a, b):
    add = a + b
    return add


print(simple(12, 45))


# Check temperature in Celsius and return it in Fahrenheit

def convert_to_fahrenheit(celsius_temp):
    calculation = celsius_temp * 1.8
    return calculation + 32


print(convert_to_fahrenheit(8))


# Some case Parameter values pass 0 or nothing:

def convert_to_fahrenheit(celsius_temp=0):
    calculation = celsius_temp * 1.8
    return calculation + 32


print(convert_to_fahrenheit())


# How to string values with integer values show in return type:

def show_string_int(value):
    return "Hello World!" + " " + str(value)


print(show_string_int(123))
