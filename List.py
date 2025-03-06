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


