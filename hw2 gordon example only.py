
# coding: utf-8

# In[1]:


import os
print(os.getcwd() + "\n")


# Basic Flask
# 
# Use Flask to create an app that runs locally, listening to a port greater than 8000. Further, the app should be able to include some kind of information from the request, perform some kind of operation on it, and return the result to the user. This is necessarily vague because there are a lot of options for using the information from a request.
# 
# I recommend that this app listen for a GET request so that you can test in a web browser. Students with more prior experience can use a POST (or other) request.

# references
#     
# debug Flask server inside Jupyter Notebook    
# https://stackoverflow.com/questions/41831929/debug-flask-server-inside-jupyter-notebook 
# 
# Using Flask to serve a machine learning model as a RESTful webservice    
# https://www.youtube.com/watch?v=s-i6nzXQF3g
#     
# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

# In[ ]:


from werkzeug.wrappers import Request, Response
from flask import Flask
from flask import request
# from flask_debugtoolbar import DebugToolbarExtension
#from flask import response

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'

#toolbar = DebugToolbarExtension(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
#    language = language.lower()
    framework = request.args.get('framework')
    ticker = request.args['ticker'] #if key doesn't exist, returns a 400, bad request error 
    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The ticker value is: {}'''.format(language, framework,ticker)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)


# http://localhost:9000/
# 
# http://localhost:9000/query-example?language=Python&framework=Flask&website=Scotch


# http://localhost:9000/query-example?ticker=GOOG 