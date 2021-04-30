#!/usr/bin/python3
"""This module starts a Flask web application.

Usage:
    Run this script with: 'python3 -m 0-hello_route'
    to start a web server running on 'http://0.0.0.0:5000/'"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays string.

    Returns:
        Return string 'Hello HBNB'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays string.

    Returns:
        Return string 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.

    Args:
        text(str): Text to show in URL.

    Return:
        String formatted.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.

    Args:
        text(str): Text to show in URL.

    Return:
        String formatted.
    """

    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
