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

