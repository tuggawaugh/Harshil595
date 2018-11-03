# Libraries

import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from flask import Flask
from iexfinance import Stock
import plotly
import plotly.plotly as plty
import plotly.graph_objs as go
import io
import base64 

app = Flask (__name__)

# Defining the function that will pull historical stock data from Yahoo! Finance
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

# Defining the Bollinger Band Function
def bb(ticker): 
    # Get Adjusted Closing Prices for Chosen Stock and Tesla between 2017-October 2018
        tick1 = get_adj_close(ticker, '1/2/2017', '31/10/2018')
        tesla = get_adj_close('tsla', '1/2/2017', '31/10/2018')
    # Calculate 30 Day Moving Average, Std Deviation, Upper Band and Lower Band
        for item in (tick1, tesla):
            item['30 Day MA'] = item['Adj Close'].rolling(window=20).mean()
            item['30 Day STD'] = item['Adj Close'].rolling(window=20).std()
            item['Upper Band'] = item['30 Day MA'] + (item['30 Day STD'] * 2)
            item['Lower Band'] = item['30 Day MA'] - (item['30 Day STD'] * 2)
    # Simple 30 Day Bollinger Band for Facebook (2016-2017)
        img = io.BytesIO()
        tick1[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
        plt.title('30 Day Bollinger Band')
        plt.ylabel('Price (USD)')
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        return '<img src="data:image/png;base64,{}">'.format(plot_url)

#Flask Apps
@app.route("/")
def index():
    return "Welcome to my flask app! Please type in http://18.222.187.92:5000/stocks/{enter ticker symbol} to see the Bollinger Band for the stock you enter.  For example, if you want to see the Bollinger Bands of Accenture's stock, enter http://18.222.187.92:5000/stocks/ACN"

@app.route("/stocks")
def stocks():
    return "Stocks"

# User enters a ticker symbol in the URL, and the string name is passed through to the bb(ticker) function to return the Bollinger Bands.
@app.route("/stocks/<string:name>/")
def getStock(name):
    return bb(name)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000)

