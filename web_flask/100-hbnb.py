#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def states_list():
    sts = storage.all('State')
    amn = storage.all('Amenity')
    plc = storage.all('Place')
    return render_template('100-hbnb.html',
                           states=sts,
                           amen=amn,
                           places=plc)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
