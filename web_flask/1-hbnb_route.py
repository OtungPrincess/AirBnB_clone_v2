#!/usr/bin/python3
"""
    This script starts a flask web application

    our web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition
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


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
