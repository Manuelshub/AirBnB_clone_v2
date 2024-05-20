#!/usr/bin/python3
"""
This Module contains a Flask Application that listens on 0.0.0.0 port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


# Route definition
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    repl = text.replace('_', ' ')
    return f"C {repl}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    repl = text.replace('_', ' ')
    return f"Python {repl}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if type(n) is int:
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    if type(n) is int:
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    # Run the Flask application.
    app.run(host='0.0.0.0', port=5000)
