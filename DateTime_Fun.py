# In Pandas several classes related to pandas\

import datetime as dt
import pandas as pd

date = pd.Timestamp(2026, 3, 12)
print(date)

Dt = pd.Timestamp(2026, 3, 12, 18, 23, 10)
print(Dt)

dateCheck = date = pd.Timestamp(dt.date(2028, 6, 27))
print(dateCheck)

dateString = pd.Timestamp('2029-10-18')
print(dateString)

dateString_both = pd.Timestamp('2029-10-18 18:05:59')
print(dateString_both)

date_series = pd.Series([pd.Timestamp('2029-10-18 18:05:59')])
print(date_series)

date_series_index = pd.Series([pd.Timestamp('2029-10-18 18:05:59')]).iloc[0]
print(date_series_index)

date_index = pd.DatetimeIndex(['2029-10-18', '2028-12-15', '2027-06-26'])
print(date_index)

# index = pd.DatetimeIndex([
#     dt.datetime(3035, 1, 12),
#     dt.datetime(3036, 2, 11),
#     dt.datetime(3037, 3, 10),
#     dt.datetime(3038, 4, 8)
# ])
#
# print(index[0])

# How-to DateRange function generated and return a DatetimeIndex holding a sequence of date

renge = pd.Series(pd.date_range(start='2025-01-01', periods=10))  # 10 dates
location = renge.iloc[2]
print(renge)
print("\nValue at index 2:", location)
fre = pd.Series(pd.date_range(start='2025-01-01', periods=20, freq='2D'))  # 2-day formation in full periods
print(fre)
business = pd.Series(pd.date_range(start='2025-01-01', periods=20, freq='B'))  # this means business daya Mon-Fri
print(business)
weekend = pd.Series(pd.date_range(start='2025-01-01', end='2025-01-31', freq='W'))  # this means only show sunday
print(weekend)

# Now We have a check to Datetime all attribute:

check = pd.Series(pd.date_range(start='2000-01-01', end='2020-12-31', freq='24D 3h'))

total_5 = check.head()
print(total_5)

# This is all attribute to check more details with:
day = check.dt.day
print(day)
month = check.dt.month
print(month)
year = check.dt.year
print(year)
hour = check.dt.hour
print(hour)
day_of_year = check.dt.day_of_year
print(day_of_year)
day_name = check.dt.day_name()
print(day_name)

# How to Work Date-offSet Object

print('Check Offset Object')

ibm = pd.read_csv('Csv_file/ibm.csv', parse_dates=['Date'], index_col='Date').sort_index()
ibm.head()

print(ibm)

stock = ibm.index
print(stock)

# To check Birthday every year
birthday = pd.date_range(start='1999-10-27', end='2023-03-31', freq='Y')
print('checking', len(birthday))

# Example with DateOffset (assuming you have a datetime object named 'stock')
stock = pd.to_datetime('2023-01-01')
off_set = stock + pd.DateOffset(day=5)
print('Now Results is', off_set)


