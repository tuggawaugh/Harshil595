from flask import Flask
app = Flask (__name__)
@app.route("/")
def hello():
    return "Hello World! This is Binta's first flask app"

if __name__ == "__main__":
    app.run('localhost', 9000, app)
    
    
    ##references
    ## http://www.patricksoftwareblog.com/steps-for-starting-a-new-flask-project-using-python3/