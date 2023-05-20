#!/usr/bin/python3
""" script that starts a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_strg(self):
    """call in the close storage method"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_template():
    """DIsplays an html page"""
    return render_template('10-hbnb_filters.html',
         states=storage.all(State), amenities=storage.all(Amenity))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
