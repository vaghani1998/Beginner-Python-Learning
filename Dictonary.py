# Dictionary is working in looks like Json data Key and Values
# same Example of dictionary

info_Stu = {'Stu_Name': 'Nency Polra',
            'Age': 25,
            'Sex': 'female',
            'Height': 5.2,
            'Nationality': 'US',
            'Clg': 'Strand Ford XYZ',
            'Hobby': 'Reading Books',
            'Phone No': '+15658254624'
            }

print(info_Stu)

Name = info_Stu['Stu_Name']
print(Name)

# How can change Name
info_Stu['Stu_Name'] = 'Jasmin Alex'
print(info_Stu)

# try to change integer values and double
info_Stu['Age'] = 23
info_Stu['Height'] = 5.4
print(info_Stu)

# Remove of index simple way:
info_Stu.pop('Phone No')
print(info_Stu)

# How to check Key is in list True or False:
name = 'Stu_Name' in info_Stu

print(name)

number = "+15658254625" in info_Stu

print(number)

value = 'Reading Books' in info_Stu.values()

print(value)

# How can Insert Key and Values pair;

info_Stu.update({"Friend": "Mishka Mesh"})
print(info_Stu)
print(len(info_Stu))

