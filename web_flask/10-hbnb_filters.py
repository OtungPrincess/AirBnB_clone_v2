#!/usr/bin/python3
"""
    This script starts a flask application
"""
from flask import Flask, render_template
from models import storage, State, City, Amenity
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
        Automatically remove session at end of request or
        app shutdown
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_states_filters():
    """
        displays html page
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                            amenities=amenities)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
