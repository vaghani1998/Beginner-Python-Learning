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

# How-to Gender of female have worked in Team of Marketing

emp_lat = pd.read_csv('Csv_file/employees.csv')

emp_female = emp_lat['Gender'] == "Female"
emp_Marketing = emp_lat['Team'] == "Marketing"

emp_lat = emp_lat[emp_female & emp_Marketing]
print(emp_lat)
emp_lat.info()

# Employees who are either senior management OR started before january 1st, 1990
print('Employees who are either senior management OR started before january 1st, 1990')
emp_lat = pd.read_csv('Csv_file/employees.csv', parse_dates=['Start Date'])

senior_Manager = emp_lat['Senior Management']
start_date = emp_lat['Start Date'] == '1993-01-01'
emp_lat = emp_lat[senior_Manager | start_date]
print(emp_lat)

# First Name is Robert who works in client Services OR start date after 01/06/2016
print('First Name is Robert who works in client Services OR start date after 01/06/2016')
emp_work = pd.read_csv('Csv_file/employees.csv', parse_dates=['Start Date']).dropna(how='all')

client_Name = emp_work['First Name'] == 'Robert'
is_client = emp_work['Team'] == 'Client Services'
is_date = emp_work['Start Date'] > '2016-06-01'
emp_work = emp_work[client_Name & is_client | is_date]
print(emp_work)

# Between Method, how-to work Dataset
# Employee Salary Between 45000 to 55000

emp_work = emp_work[emp_work['Salary'].between(130590, 14000)]
print(emp_work)
emp_work.info()

# How to duplicate Values check and find the index

emp_duplicate = pd.read_csv('Csv_file/employees.csv')

col1 = emp_duplicate[emp_duplicate['Team'].duplicated()]
duplicate = emp_duplicate[emp_duplicate['First Name'].duplicated(keep='first')]

print(col1)
print(duplicate)
emp_duplicate.info()

opposite = emp_duplicate[~emp_duplicate['First Name'].duplicated(keep=False)]
print(opposite)



