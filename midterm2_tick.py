from flask import Flask
from iexfinance import Stock

app = Flask (__name__)



def calcsr():
    
    return "" 
    # fill in with logic to calculate Sharpe Ratio




@app.route("/")
def index():
    return "Welcome to my flask app! Please type in http://127.0.0.1:5000/members/{enter your name} to get your own page"

@app.route("/hello")
def hello():
    return "Welcome to my flask app! Please type in http://127.0.0.1:5000/members/{enter your name} to get your own page"
 
@app.route("/stocks")
def stocks():
    return "Stocks"
 
@app.route("/stocks/<string:name>/")
def getStock(name):
    # get data from API - use the Python requests library
    # process input to pull out the right values needed
    # calculate the sharpe ratio 
    # return the sharpe ratio
    stock = Stock(name)  
    return str(stock.get_price())
    print(name)
 
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000)