import pandas as pd
import numpy
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime
#stock = input('What stock do you want to check? (Use the stock symbol) ')
#stock = stock.upper()
#stock = ['MSFT', 'AMZN']
stock = pd.read_csv('stocks_for_eval.csv')
tickers = stock['Ticker'].reset_index(drop=True)
df = pd.read_csv('secwiki_tickers.csv')
for stock in stock['Ticker']: 
    try:
        row = df.loc[df['Ticker'] == stock].index[0]
        name = df.iloc[row, 1]
    except:
        name = 'N/A'
    start_date = '2010-01-01'
    end_date = str(datetime.date.today())
    panel_data = data.DataReader(stock, 'yahoo', start_date, end_date)
    close = panel_data.Close
#print(name)
#print(panel_data.tail())
#print(close.head())
#print(close.tail())
#print(close.describe())
#print(type(close))
#print(panel_data.head(-5))
#fig, ax = plt.subplots(figsize=(16,9))
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(close.index, close, label=name)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    #plt.show()
    fig.savefig('Stock Price Graph for ' + stock + '.png')
    panel_data.to_csv('Stock Data for ' + stock + '.csv', encoding='utf-8', index=True)
