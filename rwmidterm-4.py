
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from flask import Flask,redirect,url_for
from flask import request
from iexfinance import Stock
import plotly
import plotly.plotly as plty
import plotly.graph_objs as go
import io
import base64 


# In[2]:


app = Flask (__name__)


# In[3]:


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


# In[ ]:


# def bb(ticker): 
#     # Get Adjusted Closing Prices for Input and Tesla between 2016-2017
#         tick1 = get_adj_close(ticker, '1/2/2017', '26/10/2018')
#         tesla = get_adj_close('tsla', '1/2/2017', '26/10/2018')
#     # Calculate 30 Day Moving Average, Std Deviation, Upper Band and Lower Band
#         for item in (tick1, tesla):
#             item['30 Day MA'] = item['Adj Close'].rolling(window=20).mean()
#             item['30 Day STD'] = item['Adj Close'].rolling(window=20).std()
#             item['Upper Band'] = item['30 Day MA'] + (item['30 Day STD'] * 2)
#             item['Lower Band'] = item['30 Day MA'] - (item['30 Day STD'] * 2)
#     # Simple 30 Day Bollinger Band for Facebook (2016-2017)
#         tick1[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
#         plt.title('30 Day Bollinger Band')
#         plt.ylabel('Price (USD)')
#         plt.show();


# In[4]:


def bb(ticker): 
    # Get Adjusted Closing Prices for Input and Tesla between 2016-2017
        tick1 = get_adj_close(ticker, '1/2/2017', '26/10/2018')
        tesla = get_adj_close('tsla', '1/2/2017', '26/10/2018')
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
        
        return '''
                <h1>Ticker Symbol: {}</h1>
                <div class="container">
                <div class="centered"><h1><form method="POST">
                <input name="name">
                <input type="submit">
                </form></h1></div></div>
                <h1><img src="data:image/png;base64,{}"></h1>
                <h1><img src="data:image/png;base64,{}"></h1>'''.format(ticker, plot_url, plot_url) 
        


# In[5]:


@app.route("/")
def index():
    return "Welcome to my flask app! Please type in http://18.222.187.92:5000/stocks/{enter ticker symbol} to see the price of the stock you enter.  For example, if you want to see the price of Accenture's stock, enter http://18.222.187.92:5000/stocks/ACN"


# In[6]:

@app.route("/stocks", methods=('GET', 'POST'))
def stocks():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('stocks',name=name))    

    name = request.args.get('name') #if key doesn't exist, returns None
    ticker=str(name)
    return bb(ticker)
    


# In[7]:


# @app.route("/stocks/<string:name>/")
# def getStock(name):
#     return bb(name)


# In[ ]:


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000)

