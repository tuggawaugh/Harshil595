
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from flask import Flask
from iexfinance import Stock


# In[2]:


app = Flask (__name__)


# In[3]:


@app.route("/")
def index():
    return "Welcome to my flask app! Please type in http://18.222.187.92:5000/stocks/{enter ticker symbol} to see the price of the stock you enter.  For example, if you want to see the price of Accenture's stock, enter http://18.222.187.92:5000/stocks/ACN"


# In[4]:


@app.route("/stocks")
def stocks():
    return "Stocks"


# In[5]:


@app.route("/stocks/<string:name>/")
def getStock(name):
    # get data from API - use the Python requests library
    # process input to pull out the right values needed
    # calculate the sharpe ratio 
    # return the sharpe ratio
    # stock = Stock(name)
    return type(name)


# In[6]:


stock = 'msft'


# In[7]:


# Make function for calls to Yahoo Finance
def get_adj_close(ticker, start, end):
    '''
    A function that takes ticker symbols, starting period, ending period
    as arguments and returns with a Pandas DataFrame of the Adjusted Close Prices
    for the tickers from Yahoo Finance
    '''
    start = start
    end = end
    info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
    return pd.DataFrame(info)


# In[8]:


# Get Adjusted Closing Prices for Input and Tesla between 2016-2017
tick1 = get_adj_close(stock, '1/2/2017', '26/10/2018')
tesla = get_adj_close('tsla', '1/2/2017', '26/10/2018')


# In[9]:


# Calculate 30 Day Moving Average, Std Deviation, Upper Band and Lower Band
for item in (tick1, tesla):
    item['30 Day MA'] = item['Adj Close'].rolling(window=20).mean()
    item['30 Day STD'] = item['Adj Close'].rolling(window=20).std()
    item['Upper Band'] = item['30 Day MA'] + (item['30 Day STD'] * 2)
    item['Lower Band'] = item['30 Day MA'] - (item['30 Day STD'] * 2)


# In[10]:


# Simple 30 Day Bollinger Band for Facebook (2016-2017)
tick1[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
plt.title('30 Day Bollinger Band')
plt.ylabel('Price (USD)')
plt.show();


# In[ ]:


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000)

