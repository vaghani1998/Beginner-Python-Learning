# How to plot create
import pandas as pd
import matplotlib.pyplot as plt

IBM = pd.read_csv('Csv_file/ibm.csv', parse_dates=['Date'], index_col="Date")

print(IBM.head())

plot = IBM.plot(y='Close')

print(plot)

Vol = IBM['Volume'].plot()

print(Vol)

# Modifying plot and templates

check = plt.style.available
print(check)

plt.style.use('fivethirtyeight')
height = IBM.plot(y='Close')
print(height)

plt.style.use('dark_background')
color = IBM.plot(y='Low')
print(color)


# How-to Visualization

def rank_performance(stock_price):
    if stock_price <= 50:
        return 'Poor'
    elif 50 < stock_price <= 100:
        return 'Satisfactory'
    else:
        return 'Excellent'


Range = IBM['Low'].apply(rank_performance).value_counts()
print(Range)

bar = Range = IBM['High'].apply(rank_performance).value_counts().plot(kind='barh')
print(bar)

avg_stock_price = IBM['Close'].mean()


def average_stock(stock_price):
    if stock_price >= avg_stock_price:
        return 'Above Average'

    return 'Below Average'


avg = IBM['Close'].apply(average_stock).value_counts()
print(avg)

avg = IBM['Close'].apply(average_stock).value_counts().plot(kind='pie', legend=True)
print('Now', avg)
