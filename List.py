# List as a container, box.
# A list is a multiple data structure that hold an ordered collection of values.
# A length of list is its number of elements.

box = ['Name', 'Address', 'City', 'Occupation']
print(box)
print(len(box))
print(type(box))
box.append("Pincode")
print(box)

contain = [4, 56, 45.2, 8, 11.1]
print(contain)
print(contain[1])

mix = ['Salary', 'Bonus', 4500, 45.2, 1100]
print(mix)
mix.pop()
print(mix)

# Check Values in list
var = 'Salary' in mix
print(var)

isNot = 'Compassion' in mix
print(isNot)


# Define functon with if more than 5 values in list True otherwise False

def is_long(is_more_then):
    if len(is_more_then) > 5:
        return True
    else:
        return False


print(is_long([1, 2, 3, 4, 5, 6]))  # Output: True
print(is_long([1, 2, 3]))


# How to particular index show in string or list data type:
# String Example
sample = 'Hello World!'

print(sample[2])
print(sample[1:3])
print(sample[:3])
print(sample[4:])
print(sample[-1])  # this values show last position values
print(sample[-2])

# List Example
data = ['Python', 'Java', 'C++', 'C#', 'Angular', 'JavaScript', 'ReactNative', 'Flutter']

print(data[2])
# print(data[9])  # it means out of range assign values that's show error
print(data[2:6])
print(data[:4])
print(data[4:])
print(data[-1])
