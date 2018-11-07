
# coding: utf-8

# In[ ]:


# import libraries

import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web  
import plotly
import plotly.plotly as plty
import plotly.graph_objs as go
import io
import base64 


# In[ ]:


# create the flask app

from flask import Flask
app = Flask (__name__)


# In[ ]:


# define a function that returns a dataframe of data from yahoo based on selected stock symbol

def get_adj_close(ticker, start, end):
    
        start = start
        end = end
        info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
        return pd.DataFrame(info)


# In[ ]:


# create the historical trend plot based on ticker input

def stockplot(ticker):
    img = io.BytesIO()
    tick1 = get_adj_close(ticker, '01/01/2016', '31/12/2017')
    tick1[['Adj Close']].plot(figsize=(10,6)) 
    plt.title('Historical Price Trend')
    plt.ylabel('Price (USD)')
    plt.savefig(img, format='png')
    img.seek(0)
    plots = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png;base64,{}">'.format(plots) 

#    df['ma50'] = pd.rolling_mean(df['Adj Close'], 50)
#    plots = df[['Adj Close', 'ma50']].plot(subplots=True, figsize=(10, 10))
#    plt.title('Historical Price Trend')
#    plt.ylabel('Price (USD)')
#    plt.savefig(img, format='png')
#    img.seek(0)
#    plots = base64.b64encode(img.getvalue()).decode()
#    return '<img src="data:image/png;base64,{}">'.format(plots)


# References 
# https://ntguardian.wordpress.com/2018/07/17/stock-data-analysis-python-v2/
# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask


# In[ ]:


# obtain ticker data for the set time period from yahoo

@app.route("/stocks/<string:name>/")
def getStock(name):
       return stockplot(name)


# In[ ]:


# run the flask app on port 9000 on the localhost

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=9000)

