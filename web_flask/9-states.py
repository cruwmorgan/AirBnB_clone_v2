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


@app.route('/states', strict_slashes=False)
def state_template():
    """display a HTML page"""
    return render_template('7-states_list.html', states=storage.all(State))


@app.route('/states/<string:id>', strict_slashes=False)
def list_by_id(id=None):
    """display a HTML page"""
    return render_template('9-states.html',
            states=storage.all(State).get('State.{}'.format(id)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
