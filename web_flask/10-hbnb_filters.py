#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb():
    """lists all cities in alphabetical order"""
    States = storage.all(State).values()
    Amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                           States=States, Amenities=Amenities)


@app.teardown_appcontext
def tear_Down(exception):
    """closes a db session or reload file storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
