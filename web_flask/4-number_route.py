#!/usr/bin/python3
'''Script that starts a flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''displays "Hello HBNB!"'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    '''displays HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    '''displays c <text>"'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
def display_python_text(text):
    '''displays Python <text>"'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def display_if_numebr(n):
    '''displays <n> is number if n is number"'''
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
