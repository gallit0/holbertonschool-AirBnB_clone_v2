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
def cities_by_states():
    s = storage.all('State')
    return render_template('8-cities_by_states.html', states=s)

@app.route("/states/<id>")
def states(id=None):
    s = storage.all('State')
    for st in s.values():
        if st.id == id:
            return render_template('9-states.html', states=s, id=st.id)
    return render_template('9-states.html', state=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
