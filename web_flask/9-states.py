#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    sts = storage.all('State')
    return render_template('9-states.html', states=sts)


@app.route("/states/<id>", strict_slashes=False)
def states_list_id(id):
    sts = storage.all('State')
    return render_template('9-states.html', states=sts, id=id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
