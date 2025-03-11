# lets me do it Missing values check
import pandas as pd

nba = pd.read_csv('Csv_file/nba.csv')
print(nba)

a1 = nba['Name'].dropna()
print(a1)

a2 = nba['Salary'].dropna(how='any')
print(a2)

a3 = nba.dropna(subset=['College', 'Team'])
print(a3)

a4 = nba.dropna(how='all')
print(a4)

drop = nba.dropna()
print(drop)


