
# coding: utf-8

# In[1]:


# import libraries

import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web  
import plotly
import plotly.plotly as plty
import plotly.graph_objs as go
import io
import base64 


# In[2]:


# create the flask app

from flask import Flask
app = Flask (__name__)


# In[3]:


# define a function that returns a dataframe of data from yahoo based on selected stock symbol using panda data reader

def get_adj_close(ticker, start, end):
    
        start = start
        end = end
        info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
        return pd.DataFrame(info)


# In[4]:


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
    
    language = request.args.get('language') 
    #if key doesn't exist, returns None
    language = language.lower()
    framework = request.args.get('framework')
    website = request.args['website'] 
    #if key doesn't exist, returns a 400, bad request error
 
    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <img src="data:image/png;base64,{}">'''.format(language, framework, plots)


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


# In[5]:


# obtain ticker data for the set time period from yahoo

@app.route("/stocks/<string:name>/")
def getStock(name):
       return stockplot(name)


# In[ ]:


# run the flask app on port 9000 on the localhost

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=9000)

