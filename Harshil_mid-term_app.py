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
import plotly
import plotly.plotly as plty
import plotly.graph_objs as go
import io
import base64

from werkzeug.wrappers import Request, Response
from flask import Flask
from flask import request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Display 'Home Page' when user navigates to Root from the URL
@app.route("/")
def index():
    return "Home Page"


# Display 'Hello World' when user navigates to /hello page
@app.route("/hello")
def hello():
    return "Hello World! Program Run #20"


# Display message requesting name when user navigates to /members page
@app.route("/members")
def members():
    return "Put your Member name in the URL"


# Display the character count of the name provided in /members/name page
@app.route("/members/<string:name>/")
def getMember(name):
    return "The length of your name " + name + " is " + str(len(name))

# Capture the ticker
@app.route("/stocks/<string:name>/")
def getTicker(name):
    ticker=str(name)
    # return ticker
    start_date = '2016-01-01'
    end_date = '2016-12-31'
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    stock_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
    # stock_data.rename(columns={stock_data.columns[1]: "Date" })
    # stock_data.columns.values[[0]]=['Date']
    # return stock_data.head()
    # return stock_data.head().to_html()

    # column_indices = [1]
    # new_names = ['Low']
    # old_names = stock_data.columns[column_indices]
    # stock_data.rename(columns=dict(zip(old_names, new_names)), inplace=True)
    # return stock_data.head().to_html()

    # stock_data.plot('Open','Close')
    # stock_data.savefig(img, format='png')
    img = io.BytesIO()
    # plt.plot(stock_data['Date'],stock_data['Close'])
    plt.plot(stock_data['Close'])
    plt.savefig(img, format='png')
    
    img.seek(0)
    
    plot_url = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png;base64,{}">'.format(plot_url)

    # return stock_data.to_html(classes='stock')
    # return '''<h1> ticker </h1>
    #          <h1> Chart </h1>'''.format(ticker, stock_data.to_html(classes='stock'))



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
    app.run(port=9000)
