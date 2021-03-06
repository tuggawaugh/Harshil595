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
        start = start
        end = end
        info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
        return pd.DataFrame(info)


def stockplot(ticker, start, end):
    try:
        img = io.BytesIO()
        tick = get_adj_close(ticker, start, end)
    #    tick('ma50') = pd.rolling_mean(df['Adj Close'], 50)
        tick[['Adj Close']].plot(figsize=(12,6)) 
    #    tick[['Adj Close', 'ma50']].plot(figsize=(10,6))
        plt.suptitle('Historical Price Trend')
        plt.ylabel('Price (USD)')
        plt.savefig(img, format='png')
        img.seek(0)
        plots = base64.b64encode(img.getvalue()).decode()

    except:
        print('exception')
        return '''
                <h1>No entry for Ticker Symbol: {}</h1>'''.format(ticker) 
    else:
        return '''<title>Historical Trend</title>
                   <h1>Historical Trend: {}  ({} - {})</h1>
                    <h3>Midterm Project: Binta Patel</h3>
    			   <form method="POST">
    			   <input name="name">
    			   <input type="submit">
    			   </form></h1>
                   <img src="data:image/png;base64,{}">'''.format(ticker, start, end, plots)
    
#@app.route("/stocks/<string:name>/")
def getStock():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('midterms.getStock', name=name))
        # Stock name is redirected back to the URL for it to be captured by Get

    name = request.args.get('name', default='MSFT')  # if key doesn't exist, returns None

    # store the ticker symbol of the stock in 'ticker' string object
    ticker = str(name)
    start_date = request.args.get('startDate', default='2016-01-01')  # if key doesn't exist, returns None
    end_date = request.args.get('endDate', default='2017-12-31')  # if key doesn't exist, returns None
    return stockplot(ticker, str(start_date), str(end_date))


def call_bpatel():
    return 'Call bpatel'

routes.append(dict(
    rule='/bpatel/',
    view_func=getStock,
    options=dict(methods=['GET', 'POST'])))


def call_bpatel_2():
    return 'call_bpatel_2'


routes.append(dict(
    rule='/bpatel_2/',
    view_func=call_bpatel_2,
    options=dict(methods=['GET', 'POST'])))
