#!/usr/bin/python3
"""
    This script starts a Flask web application:

    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable
        (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by the
        value of the text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask, render_template
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


# to set a default variable
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display4(text):
    """
        displays python then text string to screen
        on request
    """
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


# to set a specific datatype (int) for integer
@app.route('/number/<int:n>', strict_slashes=False)
def display5(n):
    """
        Displays n is a number on if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_display(n):
    """
        Displays template if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
