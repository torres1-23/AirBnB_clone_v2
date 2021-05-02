#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.

Usage :
    Execute it like this: "python3 -m web_flask.8-cities_by_states_list"
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """Displays an HTML page.

    Return:
        HTML page.
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
