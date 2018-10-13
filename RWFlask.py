
# coding: utf-8

# In[ ]:


from flask import Flask


# In[ ]:


app = Flask (__name__)
@app.route("/")
def hello():
    return "Hello World! This is Rich Williams' first flask app. I am testing my own app to see if I can get this thing running!"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=9000)
    
    
    ##references
    ## http://www.patricksoftwareblog.com/steps-for-starting-a-new-flask-project-using-python3/

