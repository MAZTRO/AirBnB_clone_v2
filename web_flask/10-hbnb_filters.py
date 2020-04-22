#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def states_list():
    sts = storage.all('State')
    amn = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=sts, amen=amn)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
