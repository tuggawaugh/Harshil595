"""
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import io
import base64
from pandas import DataFrame, Series
from pandas_datareader import data
from datetime import datetime
from flask import Flask, redirect, url_for
from flask import request

routes = []

def hello_hshah():
    return "Use the http://18.223.99.235:9000/stocks?name=XXX URL " \
           "format where XXX is the Ticker Symbol"


# Capture Ticker from URL using both Get (from URL) & Post methods (Searchbox)
#@mod.route("/stocks", methods=('GET', 'POST'))
def stocks_hshah():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('midterms.stocks_hshah', name=name))
        # Stock name is redirected back to the URL for it to be captured by Get

    name = request.args.get('name', default='MSFT')  # if key doesn't exist, returns None

    # store the ticker symbol of the stock in 'ticker' string object
    ticker = str(name)
    # set the start and end date and the first and last day of FY2016
    start_date = '2016-01-01'
    end_date = '2016-12-31'
    # User pandas_reader.data.DataReader to load the desired stock and
    # S&P ('spy') data into respective frames using Yahoo's API
    stock_data = pd.DataFrame()
    spy_data = pd.DataFrame()
    stock_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
    spy_data = data.DataReader('SPY', 'yahoo', start_date, end_date)

    # Plot the graphs using matplotlib and encode them using base64 to
    # publish them on the HTML
    img11 = io.BytesIO()
    plt.clf()
    # subplot feature is used to show the side-by-side comparison of the
    # stock and S&P's performance
    fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True)
    ax = axs[0]
    ax.plot(stock_data['Close'], marker='', linestyle='-')
    ax.set_title(ticker+' Close Price (2016)')

    ax = axs[1]
    ax.plot(spy_data['Close'], marker='', linestyle='-')
    ax.set_title('S&P 500 Close Price (2016)')

    # Rotate date labels automatically
    fig.autofmt_xdate()
    plt.show()

    # Encode and publish the Graph
    fig.suptitle(ticker+' v S&P 500 Comparison (2016)')
    plt.savefig(img11, format='png')
    img11.seek(0)
    plot1_url = ""
    plot1_url = base64.b64encode(img11.getvalue()).decode()

    return '''<h1>Ticker Symbol: {}</h1>
            <form method="POST">
            <input name="name">
            <input type="submit">
            </form></h1>
            <img src="data:image/png;base64,{}">'''.format(ticker, plot1_url)
            
def call_hshah():
    return 'Call hshah'


routes.append(dict(
    rule='/hshah/',
    view_func=stocks_hshah,
    options=dict(methods=['GET', 'POST'])))


def call_hshah_2():
    return 'call_hshah_2'


routes.append(dict(
    rule='/hshah_help/',
    view_func=hello_hshah,
    options=dict(methods=['GET', 'POST'])))
