from flask import Flask
app = Flask (__name__)
@app.route("/")
def hello():
    return "Hello World! This is Team Accenture's first flask app. We are testing ATTEMPT 2!"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=9000)
    
    
    ##references
    ## http://www.patricksoftwareblog.com/steps-for-starting-a-new-flask-project-using-python3/