#!/usr/bin/python3
"""Python module that returns string when navigating to root directory"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Return the welcome message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Return HBNB when navigated to"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    """Route /c/<text> returns C message"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
