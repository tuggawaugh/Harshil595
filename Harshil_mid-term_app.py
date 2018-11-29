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

# Display 'Home Page' when user navigates to Root from the URL 
@app.route("/") 
def index(): 
    return "Hello World! Mid-Term Flask App by Harshil Shah" 
 
 
# Display 'Instruction message' when user navigates to /help page 
@app.route("/help") 
def hello(): 
    return "Enter the Ticker Symbol in the Searchbox" 
  
# Capture the ticker
@app.route("/stocks", methods=('GET', 'POST'))
def stocks():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('stocks',name=name))    

    name = request.args.get('name') #if key doesn't exist, returns None
    ticker=str(name)
    # return ticker
    start_date = '2016-01-01'
    end_date = '2016-12-31'
    # User pandas_reader.data.DataReader to load the desired data. As simple as that. 
    stock_data = pd.DataFrame() 
    spy_data = pd.DataFrame() 
    stock_data = data.DataReader(ticker, 'yahoo', start_date, end_date) 
    spy_data = data.DataReader('SPY', 'yahoo', start_date, end_date) 
  

    img11 = io.BytesIO() 
    plt.clf()
# Now switch to a more OO interface to exercise more features.
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

# Publish the Graph
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
