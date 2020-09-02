#!/usr/bin/python3
'''Script that starts a Flask application'''


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_method(self):
    '''teardown'''
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    '''displas HTML page'''
    states = storage.all('State')
    return render_template('8-cities_by_state.html', states=states)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
