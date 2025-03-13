# lets me do it Missing values check Also Fill '0', '' values
import pandas as pd

nba = pd.read_csv('Csv_file/nba.csv')
print(nba)

a1 = nba['Name'].dropna()
print(a1)

a2 = nba['Salary'].dropna(how='any')
print(a2)

a3 = nba.dropna(subset=['College', 'Team'])
print(a3)

a5 = nba.dropna(how='all')
print(a5)

drop = nba.dropna()
print(drop)

# How can Be Missing values fill to fillna() Method

nba["Salary"] = nba["Salary"].fillna(0)

print(nba)

nba['College'] = nba['College'].fillna(value='Something etc')

print(nba)

last_correct = nba.fillna(0.0)

print(last_correct)  # its means all string or data datatype also fill to 0.0

print(nba.info())

# How to astype means Datatype of column check

nba['Salary'] = nba['Salary'].astype(int)

print(nba)

print(nba.dtypes)

# How to reduce the file Size

nba.info()

nba['Position'] = nba['Position'].astype('category')

nba['Team'] = nba['Team'].astype('category')

print(nba)

nba.info()





