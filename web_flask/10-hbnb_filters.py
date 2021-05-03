#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.

Usage :
    Execute it like this: "python3 -m web_flask.9-states.py"
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLAlchemy session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Displays an HTML page with a list of all
    States instances."""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
