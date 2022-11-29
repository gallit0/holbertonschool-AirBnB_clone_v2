#!/usr/bin/python3
"""
Module 7-states_list.py
"""
from flask import Flask, render_template
from models import storage
from models import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def deletesql():
        storage.close()


@app.route("/states_list")
def number_odd_or_even_route():
        return render_template("7-states_list.html", storage.all(State))


if __name__ == '__main__':
        app.run(host=('0.0.0.0'),
                port=int('5000'), threaded=True)
