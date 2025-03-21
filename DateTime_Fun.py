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