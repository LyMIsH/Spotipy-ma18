from core.datahandling.data import Data
from flask import Flask
from core.datahandling import search


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_artists():
    return search.get_artists()


def start():
    app.run(host='0.0.0.0', port=5050, use_reloader=False, debug=True)
