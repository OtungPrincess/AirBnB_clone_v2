#!/usr/bin/python3
"""
    This script starts a Flask web application:

    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display1():
    """ returns Hello HBNB to screen when requested """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display2():
    """ returns HBNB to screen """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display3(text):
    """ returns C then text string to screen """
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
