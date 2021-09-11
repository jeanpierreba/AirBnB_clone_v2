#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a message at the root route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string at the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ Returns a string at the /c route """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is_cool'):
    """ Returns a string at the /python route """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    """ Returns a string at the /number route """
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    """ Run web application """
    app.run(host='0.0.0.0', port=5000)
