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

from app.simple_page import module1

app = Flask(__name__)

# Display 'Home Page' when user navigates to Root from the URL 
@app.route("/") 
def index(): 
    return "Home Page" 
 
# Set the flask app to run at port 9000 
if __name__ == "__main__": 
    app.run(host = '0.0.0.0', port=9000) 
