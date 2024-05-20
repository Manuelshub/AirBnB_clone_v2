#!/usr/bin/python3
"""
This Module contains a Flask Application that listens on 0.0.0.0 port 5000
"""

from flask import Flask

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


if __name__ == "__main__":
    # Run the Flask application.
    app.run(host='0.0.0.0', port=5000)
