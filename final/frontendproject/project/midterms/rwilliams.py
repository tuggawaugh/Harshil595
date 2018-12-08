"""
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pandas_datareader import data as web  
from flask import Flask,redirect,url_for
from flask import Blueprint, render_template
from flask import request
import io
import base64 

routes = []


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
    try:
    # Get Adjusted Closing Prices for Chosen Stock and Tesla between Jan 2016 - December 2017
        tick1 = get_adj_close(ticker, '1/1/2016', '31/12/2017')
        tesla = get_adj_close('tsla', '1/1/2016', '31/12/2017')
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
    except:
        print('exception')
        return '''
                <h1>No entry for Ticker Symbol: {}</h1>'''.format(ticker) 
    else:
        return '''<h1>30 Day Bollinger Bands for ticker: {}  (Jan 2016 - Dec 2017)</h1>
                <h3>Midterm Project: Richard Williams</h3>
				<form method="POST">
				<input name="name">
				<input type="submit">
				</form></h1>
				<img src="data:image/png;base64,{}">'''.format(ticker, plot_url)

#Flask Apps
#@app.route("/")
#def index():
#    return "Welcome to my flask app! Please type in http://18.222.187.92:5000/stocks/{enter ticker symbol} to see the Bollinger Band for the stock you enter.  For example, if you want to see the Bollinger Bands of Accenture's stock, enter http://18.222.187.92:5000/stocks/ACN"

#@app.route("/stocks")
def stocks():
    return "Stocks"

# User enters a ticker symbol in the URL, and the string name is passed through to the bb(ticker) function to return the Bollinger Bands.
#@app.route("/stocks/<string:name>/")
def getStock_rwilliams():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('midterms.getStock_rwilliams', name=name))
        # Stock name is redirected back to the URL for it to be captured by Get

    name = request.args.get('name', default='MSFT')  # if key doesn't exist, returns None

    # store the ticker symbol of the stock in 'ticker' string object
    ticker = str(name)
    
    return bb(name)


def call_rwilliams():
    return 'Call rwilliams'


routes.append(dict(
    rule='/rwilliams/',
    view_func=getStock_rwilliams,
    options=dict(methods=['GET', 'POST'])))


def call_rwilliams_2():
    return 'call_rwilliams_2'


routes.append(dict(
    rule='/rwilliams_2/',
    view_func=call_rwilliams_2,
    options=dict(methods=['GET', 'POST'])))
