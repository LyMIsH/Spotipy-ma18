from flask import Flask
from flask import request
from core.datahandling import search
from core.account import account_managment
from core.logging import logger
from flask import jsonify


app = Flask(__name__)
user = None
USER_NOT_LOGGED_MESSAGE = "Not logged in"


def is_logged(func):
    def wrapper(*args, **kwargs):
        if user is not None:
            val = func(*args, **kwargs)
            return val
        return USER_NOT_LOGGED_MESSAGE

    wrapper.__name__ = func.__name__  # Fixed unknown exception
    return wrapper


@app.route('/login', methods=['GET', 'POST'])
def login():
    global user
    username = request.args.get('username')
    password = request.args.get('password')
    if username is None or password is None:
        return "Error in parameters"
    else:
        user = account_managment.login(username, password)
        logger.info(f"User {username} logged in from {request.remote_addr}")
        return "Logged in"


@app.route('/artists', methods=['GET'])
@is_logged
def get_artists():
    return str(search.get_artists(premium=user.is_premium))


@app.route('/albums', methods=['GET'])
@is_logged
def get_albums():
    artist_id = request.args.get('id')
    if artist_id is None:
        return "Artist id not supplied"
    return str(search.get_albums(artist_id, premium=user.is_premium))


@app.route('/toptracks', methods=['GET'])
@is_logged
def get_top_artist_tracks():
    artist_id = request.args.get('id')
    if artist_id is None:
        return "Artist id not supplied"
    return str(search.get_top_artist_tracks(artist_id, premium=user.is_premium))


@app.route('/albumtracks', methods=['GET'])
@is_logged
def get_album_tracks():
    album_id = request.args.get('id')
    if album_id is None:
        return "Album id not supplied"
    return str(search.get_album_tracks(album_id, premium=user.is_premium))


def start():
    app.run(host='0.0.0.0', port=5050, use_reloader=False, debug=True)
