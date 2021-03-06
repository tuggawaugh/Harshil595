
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web  
import plotly
import plotly.plotly as plty
import plotly.graph_objs as go
import io
import base64 


# In[2]:


# creates the flask app
from flask import Flask
app = Flask (__name__)


# In[3]:


def get_adj_close(ticker, start, end):
    
        start = start
        end = end
        info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
        return pd.DataFrame(info)


# In[4]:


#ticker = 'msft'


# In[5]:


#tick1 = get_adj_close(ticker, '1/2/2017', '26/10/2018')


# In[6]:


def stockplot(ticker):
    img = io.BytesIO()
    tick1 = get_adj_close(ticker, '1/2/2017', '26/10/2018')
    tick1[['Adj Close']].plot(figsize=(12,6)) 
    plt.title('Price History')
    plt.ylabel('Price (USD)')
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png;base64,{}">'.format(plot_url)
    
# reference https://ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/


# In[7]:


# obtain ticker date for the set time period from quandl
@app.route("/stocks/<string:name>/")
def getStock(name):
       return stockplot(name)
    


# In[8]:


# #from Gordon's example to return output

# @app.route('/query-example')
# def query_example():
#     language = request.args.get('language') #if key doesn't exist, returns None
# #    language = language.lower()
#     framework = request.args.get('framework')
#     ticker = request.args['ticker'] #if key doesn't exist, returns a 400, bad request error 
#     return '''<h1>The language value is: {}</h1>
#               <h1>The framework value is: {}</h1>
#               <h1>The ticker value is: {}'''.format(language, framework,ticker)


# In[9]:


# # run the flask app on port 9000 on the localhost
# if __name__ == "__main__":
#     app.run('localhost', 9000, app)


# In[ ]:


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=9000)


# In[ ]:


# References
# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

