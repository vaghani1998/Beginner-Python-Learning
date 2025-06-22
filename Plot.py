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
