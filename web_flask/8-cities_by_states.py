#!/usr/bin/python3
"""script that starts a Flask web application:"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """After each request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def state_template():
    """display a HTML page"""
    all_state = storage.all(State)
    return render_template('8-cities_by_states.html', states=all_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
