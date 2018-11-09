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
from flask import Flask,redirect,url_for
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
  
    img1 = io.BytesIO() 
    plt.plot(stock_data['Close']) 
    plt.savefig(img1, format='png') 
    img1.seek(0)
    plot1_url = ""
    plot1_url = base64.b64encode(img1.getvalue()).decode() 

    img2 = io.BytesIO() 
    plt.plot(spy_data['Close']) 
    plt.savefig(img2, format='png') 
    img2.seek(0) 
    plot2_url = ""
    plot2_url = base64.b64encode(img2.getvalue()).decode() 
     
    return '''<form method="POST">
            <input name="name">
            <input type="submit">
            </form></h1>
            <img src="data:image/png;base64,{}"></h1>
            <img src="data:image/png;base64,{}">'''.format(plot1_url,plot2_url) 
 
 
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
