#%matplotlib inline

import numpy as np
import pandas as pd
import quandl 
from pandas import DataFrame, Series 
from pandas_datareader import data
#import talib
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter
import plotly
import plotly.plotly as plty
import plotly.graph_objs as go
import io
import base64

from werkzeug.wrappers import Request, Response
from flask import Flask,redirect,url_for
from flask import request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Display 'Hello Message on Home Page' when user navigates to Root from the URL 
@app.route("/") 
def index(): 
    return "Hello World! Mid-Term Flask App by Harshil Shah to compare a stock's performance with S&P 500 for calendar year 2016" 
  
# Display 'Instruction message' when user navigates to /help page 
@app.route("/help") 
def hello(): 
    return "Use the http://18.223.99.235:9000/stocks?name=XXX URL format where XXX is the Ticker Symbol" 
  
# Capture the ticker from the URL using both Get (from URL) and Post methods (Searchbox)
@app.route("/stocks", methods=('GET', 'POST'))
def stocks():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('stocks',name=name)) #Stock name is redirected back to the URL for it to be captured by Get

    name = request.args.get('name') #if key doesn't exist, returns None
    
    # store the ticker symbol of the stock in 'ticker' string object
    ticker=str(name)
    # set the start and end date and the first and last day of FY2016
    start_date = '2016-01-01'
    end_date = '2016-12-31'
    # User pandas_reader.data.DataReader to load the desired stock and S&P ('spy') data into respective frames using Yahoo's API
    stock_data = pd.DataFrame() 
    spy_data = pd.DataFrame() 
    stock_data = data.DataReader(ticker, 'yahoo', start_date, end_date) 
    spy_data = data.DataReader('SPY', 'yahoo', start_date, end_date) 
  
    # Plot the graphs using matplotlib and encode them using base64 to publish them on the HTML
    img11 = io.BytesIO() 
    plt.clf()
    # subplot feature is used to show the side-by-side comparison of the stock and S&P's performance
    fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True)
    ax = axs[0]
    ax.plot(stock_data['Close'], marker='', linestyle='-')
    ax.set_title(ticker+' Close Price (2016)')

    ax = axs[1]
    ax.plot(spy_data['Close'], marker='', linestyle='-')
    ax.set_title('S&P 500 Close Price (2016)')

    ## Rotate date labels automatically
    fig.autofmt_xdate()
    plt.show()

    # Encode and publish the Graph
    fig.suptitle(ticker+' v S&P 500 Comparison (2016)')
    plt.savefig(img11, format='png') 
    img11.seek(0)
    plot1_url = ""
    plot1_url = base64.b64encode(img11.getvalue()).decode()     
     
    return '''<form method="POST">
            <input name="name">
            <input type="submit">
            </form></h1>
            <img src="data:image/png;base64,{}">'''.format(plot1_url) 
 
 
@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    language = language.lower()
    framework = request.args.get('framework')
    website = request.args['website'] #if key doesn't exist, returns a 400, bad request error

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)
 
 
# Set the flask app to run at port 9000 
if __name__ == "__main__": 
    app.run(host = '0.0.0.0', port=9000) 
