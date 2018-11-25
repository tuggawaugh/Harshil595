simple_page = Blueprint('simple_page', __name__, template_folder='templates')

 
# Display 'Hello World' when user navigates to /hello page 
@module1.route("/hello") 
def hello(): 
    return "Hello World! Program Run #20" 
 
 
# Display message requesting name when user navigates to /members page 
@module1.route("/members") 
def members(): 
    return "Put your Member name in the URL" 
 
 
# Display the character count of the name provided in /members/name page 
@module1.route("/members/<string:name>/")
def getMember(name):
    return "The length of your name " + name + " is " + str(len(name)) 
 
# Capture the ticker
@module1.route("/stocks", methods=('GET', 'POST'))
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

# Format the Dates
#    myDates = [datetime(2012,1,i+3) for i in range(10)]
#    myValues = [5,6,4,3,7,8,1,2,5,4]
#    fig, ax = plt.subplots()
#    ax.plot(myDates,myValues)


    ## Rotate date labels automatically
    fig.autofmt_xdate()
    plt.show()

# Publish the Graph
    fig.suptitle(ticker+' v S&P 500 Comparison')
    plt.savefig(img11, format='png') 
    img11.seek(0)
    plot1_url = ""
    plot1_url = base64.b64encode(img11.getvalue()).decode() 
    

    # img11 = ""
#    img11 = io.BytesIO() 
#    plt.clf()
#    plt.plot(stock_data['Close']) 
#    plt.title(ticker, loc='left')
#    plt.savefig(img11, format='png') 
#    img11.seek(0)
#    plot1_url = ""
#    plot1_url = base64.b64encode(img11.getvalue()).decode() 
#
#    # img22 = ""
#    img22 = io.BytesIO() 
#    # plt.clf()
#    plt.plot(spy_data['Close']) 
#    plt.savefig(img22, format='png') 
#    img22.seek(0) 
#    plot2_url = ""
#    plot2_url = base64.b64encode(img22.getvalue()).decode() 
#

     
    return '''<form method="POST">
            <input name="name">
            <input type="submit">
            </form></h1>
            <img src="data:image/png;base64,{}">'''.format(plot1_url) 
 
 
@module1.route('/query-example')
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
