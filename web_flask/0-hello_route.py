#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

# Route definition
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    # Run the Flask application.
    app.run(host='0.0.0.0', port=5000)
