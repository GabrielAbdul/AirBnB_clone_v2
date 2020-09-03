#!/usr/bin/python3
'''Script that starts a Flask web application'''


from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_method(self):
    '''calls storage.close()'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def show_states_list_html():
    '''displays states_list html page'''
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
