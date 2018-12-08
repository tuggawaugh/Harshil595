"""
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pandas_datareader import data as web
from pandas_datareader._utils import RemoteDataError
from flask import Flask,redirect,url_for
from flask import Blueprint, render_template
from flask import request
import io
import base64 
import numpy as np

routes = []


'''def call_grubin():
'''

def stocks():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('midterms.stocks',name=name))    

    name = request.args.get('name', default='MSFT') #if key doesn't exist, returns None
    ticker=str(name)
    return bb(ticker)

"""    return 'Call grubin'
"""

routes.append(dict(
    rule='/grubin/',
    view_func=stocks,
    options=dict(methods=['GET', 'POST'])))

def call_grubin_2():
    return 'call_grubin_2'


routes.append(dict(
    rule='/grubin_2/',
    view_func=call_grubin_2,
    options=dict(methods=['GET', 'POST'])))

def get_adj_close(ticker, start, end):
        '''
        A function that takes ticker symbols, starting period, ending period
        as arguments and returns with a Pandas DataFrame of the Adjusted Close Prices
        for the tickers from Yahoo Finance
        '''
        start = start
        end = end
        try:
            info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
            return pd.DataFrame(info)
        except RemoteDataError:
            print("No information for ticker '%s'" % ticker)
            return -1

def rsiFunc(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi




def bb(ticker):
    try:
        # Get Adjusted Closing Prices for Input
        tick1 = get_adj_close(ticker, '1/1/2016', '31/12/2017')

        # Calculate RSI        
        tick1['rsi'] = rsiFunc(tick1['Adj Close'], 14)
        
        img = io.BytesIO()
        
        fig = plt.figure(figsize=(12, 6)) 
        gs = gridspec.GridSpec(2, 1, width_ratios=[1], height_ratios=[3,1]) 
        ax0 = plt.subplot(gs[0])
        ax0.plot(tick1[['Adj Close']])
        ax1 = plt.subplot(gs[1])
        ax1.plot(tick1['rsi'])
        fig.autofmt_xdate()
        
#        plt.tight_layout()
 
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
#        
#        left  = 0.125  # the left side of the subplots of the figure
#        right = 0.9    # the right side of the subplots of the figure
#        bottom = 0.1   # the bottom of the subplots of the figure
#        top = 0.9      # the top of the subplots of the figure
#        wspace = 0.2   # the amount of width reserved for blank space between subplots
#        hspace = 0.9   # the amount of height reserved for white space between subplots
# 
        ax0.set_title('Price')
        ax0.set_ylabel('Price (USD)')
        ax1.set_ylabel('RSI')
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
    except:
        print('exception')
        return '''
                <h1>No entry for Ticker Symbol: {}</h1>'''.format(ticker) 
    else:
        return '''
                <h1>Relative Stregnth Index for ticker: {}  (Jan 2016 - Dec 2017)</h1>
                <h3>Relative Stregnth Index (RSI) is ipsum ... </h3>
                <div class="container">
                <div class="centered"><h1><form method="POST">
                <input name="name">
                <input type="submit">
                </form></h1></div></div>
                <h1><img src="data:image/png;base64,{}"></h1>'''.format(ticker, plot_url) 
        
