
# coding: utf-8

# ## FE595 Fall 2018 Midterm 

# In[2]:


# import libraries

import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web  
import plotly
import plotly.plotly as plty
import plotly.graph_objs as go
import io
import base64 


# In[3]:


# create the flask app

from flask import Flask
app = Flask (__name__)


# In[4]:


# define a function that returns a dataframe sourced from yahoo data for a given stock symbol using 
# panda data reader to connect

def get_adj_close(ticker, start, end):
    
        start = start
        end = end
        info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
        return pd.DataFrame(info)


# In[5]:


# create a function that outputs a historical trend plot based on ticker input

def stockplot(ticker):
    img = io.BytesIO()
    tick = get_adj_close(ticker, '01/01/2016', '31/12/2017')
#    tick('ma50') = pd.rolling_mean(df['Adj Close'], 50)
    tick[['Adj Close']].plot(figsize=(10,6)) 
#    tick[['Adj Close', 'ma50']].plot(figsize=(10,6))
    plt.title('Historical Price Trend')
    plt.ylabel('Price (USD)')
    plt.savefig(img, format='png')
    img.seek(0)
    plots = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png;base64,{}">'.format(plots)

# References 
# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
# https://ntguardian.wordpress.com/2018/07/17/stock-data-analysis-python-v2/


# In[6]:


# based on the stock ticker symbol that is entered at the end of the url, the stockplot function will be 
# invoked and return a historical trend plot for a 1 year period from Jan 1 2016 to Dec 31 2017

@app.route("/stocks/<string:name>/")
def getStock(name):
       return stockplot(name)


# In[ ]:


# when user navigates to /helloworld when the flask app is running, text specified below will be displayed.

@app.route("/helloworld")
def hello():
    return "Hello World! This is Binta's first flask app"


# In[ ]:


# run the flask app on port 9000 on the localhost

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=9000)

