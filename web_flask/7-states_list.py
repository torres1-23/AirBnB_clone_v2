#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.

Usage :
    Execute it like this: "python3 -m web_flask.7-states_list"
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page.

    Return:
        HTML page.
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
