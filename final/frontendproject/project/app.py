"""
"""

from flask import Flask, render_template

app = Flask(__name__)

app.debug = True


from midterms import mod
app.register_blueprint(mod, url_prefix='/midterms')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2.html')
def index2():
    return render_template('index2.html')


#@app.route('/midterms')
#def hello():
#    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
