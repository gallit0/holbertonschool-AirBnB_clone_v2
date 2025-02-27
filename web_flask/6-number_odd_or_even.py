#!/usr/bin/python3
"""
flask
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """
    hbnb
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    hbnb
    """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """
    C is fun
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python(text='is cool'):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    if n % 2 == 0:
        res = '{} is even'.format(n)
    else:
        res = '{} is odd'.format(n)
    return render_template('6-number_odd_or_even.html', result=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
