#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Method to print a message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Method to print a message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text_C(text):
    """ Method to print a message """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', strict_slashes=False, defaults={'word': 'is cool'})
@app.route('/python/(<text>)', strict_slashes=False)
def show_text_PY(text):
    """ Method to print a message """
    return 'Python {}'.format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
