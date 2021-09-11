#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Returns a template at the /number_template/<n> route """
    return render_template('5-number.html', value=n)


if __name__ == "__main__":
    """ Run web application """
    app.run(host='0.0.0.0', port=5000)
