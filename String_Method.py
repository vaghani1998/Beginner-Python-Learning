# a method is like a function that belongs to object

# Upper_case
occupation = "software developer"
check = occupation.upper()
print(check)

# Lower_case
country = "United Of America"
check1 = country.lower()
print(check1)

# Swap_case
movie = 'Avatar Movie is Best'
check2 = movie.swapcase()
print(check2)

# Title
name = 'Jasmin Alexa'
check3 = name.title()
print(check3)

# Capitalize
name = 'Jasmin Alexa'
check4 = name.capitalize()
print(check4)

# Right & Left Space Remove Method
developer = "     Python Developer     "
left = developer.lstrip()
right = developer.rstrip()
both = developer.lstrip().rstrip()
simple = developer.strip()
print(left)
print(right)
print(both)
print(simple)

# Split Values
city = 'New York'
country = 'US'
combined = f"{city}, {country}"
split = combined.split(',')
print(split)

# Replace Values
hospital = 'P P Savani'
check5 = hospital.replace('S', 'M')
print(check5)
