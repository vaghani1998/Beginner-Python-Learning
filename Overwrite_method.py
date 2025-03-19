# How can Overwrite method and Replace method.

import pandas as pd

employee = pd.read_csv('Csv_file/employees.csv')

employee = employee.set_index('First Name')

employee = employee['Team'].loc['Larry']

print(employee)

# now, does it replace method?

emp = pd.read_csv('Csv_file/employees.csv')

emp["Team"] = emp["Team"].str.replace("Marketing", "MBA Marketing")

print(emp)


# Apply Method

bond = pd.read_csv('Csv_file/employees.csv')


def team_renk(row):
    depart = row.loc['Team']
    bonus = row.loc['Bonus %']

    if depart == ['Marketing']:
        return 'Granted'

    if bonus > 5.0:
        return 'Are you brilliant'

    return 'No comments'


apply = bond.apply(team_renk, axis='columns')
print(apply)

# How to split values

bond['First Name'] = bond['First Name'] = 'Alexa, Donald trump'

bond[['First', 'Last']] = bond['First Name'].str.split(",", expand=True)

print(bond)

# How can set indexing

bond = pd.read_csv('Csv_file/employees.csv')

bond = bond.set_index('Team')

both = bond.set_index(keys=["First Name", "Start Date"]).head(15).sort_index()

print(both)

# How to get_level_values method extracts an index with the values from one level in the multiple.

multi = pd.read_csv('Csv_file/employees.csv', parse_dates=['Start Date'], date_format='%m-%d-%Y', index_col=['Start Date', 'First Name', 'Team']).sort_index()

level = multi.index.get_level_values('Start Date')
date = level.get_level_values(0)
print(date)

level1 = multi.index.get_level_values('Team')
name = level1.get_level_values(0)
print(name)

print(multi)
multi.info()

# How to rename index level then multiple index level:

index = multi.index.set_names(names='Date', level=0).to_frame().iloc[5:9]

index1 = multi.index.set_names(names='Name', level=1)

print('hallo world!', index)
print(index1)

# I order data Team and Start date wise:

exe = pd.read_csv('Csv_file/employees.csv', parse_dates=['Start Date'], date_format='%m-%d-%Y')
exe['Team'] = exe['Team'].fillna('Sales Mens')
exe = exe.set_index(keys=['Team', 'Start Date'])
# exe = exe.sort_index(ascending=False)
exe = exe.sort_index(ascending=[True, False])

exe.info()
print(exe)

# How to Tuple format in values:
extract = pd.read_csv('Csv_file/employees.csv', parse_dates=['Start Date'], date_format='%m-%d-%Y', index_col=['Team', 'Start Date']).sort_index()
index_tru = tuple(extract.index[2:6])
print(index_tru)
print(extract)