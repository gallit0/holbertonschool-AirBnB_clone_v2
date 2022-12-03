#!/usr/bin/python3
"""
flask
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exit):
    storage.close()


@app.route("/hbnb_filters")
def index():
    s = storage.all('State').values()
    a = storage.all('Ameity').values()
    return render_template('6-index.html', states=s, amenities=a)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
