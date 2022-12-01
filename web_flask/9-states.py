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


@app.route("/states")
@app.route("/states/<id>")
def cities_by_states(id=None):
    s = storage.all('State')
    if id is not None:
        for i in s:
            sp = i.split('.')
            if sp[1] != id:
                del s[sp]
    return render_template('8-cities_by_states.html', states=s)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
