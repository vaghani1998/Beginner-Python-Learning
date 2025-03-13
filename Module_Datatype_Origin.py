# How-to Modules Data formations also reduce file size

import pandas as pd

emp = pd.read_csv('Csv_file/employees.csv')

emp['Start Date'] = pd.to_datetime(emp["Start Date"], errors='coerce').dt.strftime('%d/%m/%Y')
emp['Last Login Time'] = pd.to_datetime(emp['Last Login Time'], format='%H:%M %p', errors='coerce').dt.strftime("%H:%M %p")
emp['Gender'] = emp['Gender'].astype('category')
emp['First Name'] = emp['First Name'].fillna('Alexa')
emp['Gender'] = emp['Gender'].fillna('Male')
emp['Senior Management'] = emp['Senior Management'].astype(bool).fillna(bool)
emp['Team'] = emp['Team'].fillna('Government')

print(emp.head(10))
emp.info()

# How-to Data Filter in dataset (calculation)

emp["Team"] = emp["Team"] == "Marketing"
emp['Salary'] = emp['Salary'] > 130590
var = emp[emp['Bonus %'] < 4.17]
print(var)
print(emp)
emp.info()





