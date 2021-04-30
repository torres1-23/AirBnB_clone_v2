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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
