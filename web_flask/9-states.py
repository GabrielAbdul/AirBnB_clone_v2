#!/usr/bin/python3
'''Script that starts a Flask application'''


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_method(self):
    '''teardown'''
    storage.close()


@app.route('/states')
def states():
    '''displas HTML page'''
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_id(id=None):
    '''displas HTML page'''
    states = storage.all(State)
    s_id = states.get('State.' + str(id))
    return render_template('9-states.html', states=states, s_id=s_id)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
