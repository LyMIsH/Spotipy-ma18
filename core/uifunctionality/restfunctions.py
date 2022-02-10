from flask import Flask
from flask import request
from core.datahandling import search
from core.account import account_managment
from core.logging import logger
import config


app = Flask(__name__)
users_by_ip = dict()
USER_NOT_LOGGED_MESSAGE = "Not logged in"


def is_logged(addr):
    return addr in users_by_ip.keys()


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username is None or password is None:
        return "Error in parameters"
    else:
        users_by_ip[request.remote_addr] = account_managment.login(username, password)
        logger.info(f"User {username} logged in from {request.remote_addr}")
        return "Logged in"


@app.route('/artists', methods=['GET'])
def get_artists():
    if not is_logged(request.remote_addr): return USER_NOT_LOGGED_MESSAGE
    return str(search.get_artists(premium=users_by_ip[request.remote_addr].is_premium))


@app.route('/albums', methods=['GET'])
def get_albums():
    if not is_logged(request.remote_addr): return USER_NOT_LOGGED_MESSAGE
    artist_id = request.args.get('id')
    if artist_id is None:
        return "Artist id not supplied"
    return str(search.get_albums(artist_id, premium=users_by_ip[request.remote_addr].is_premium))


@app.route('/toptracks', methods=['GET'])
def get_top_artist_tracks():
    if not is_logged(request.remote_addr): return USER_NOT_LOGGED_MESSAGE
    artist_id = request.args.get('id')
    if artist_id is None:
        return "Artist id not supplied"
    return str(search.get_top_artist_tracks(artist_id, premium=users_by_ip[request.remote_addr].is_premium))


@app.route('/toptracks-genre', methods=['GET'])
def get_top_genre_tracks():
    if not is_logged(request.remote_addr): return USER_NOT_LOGGED_MESSAGE
    genre = request.args.get('genre')
    if genre is None:
        return "Genre not supplied"
    return str(search.get_top_genre_tracks(genre, premium=users_by_ip[request.remote_addr].is_premium))


@app.route('/albumtracks', methods=['GET'])
def get_album_tracks():
    if not is_logged(request.remote_addr): return USER_NOT_LOGGED_MESSAGE
    album_id = request.args.get('id')
    if album_id is None:
        return "Album id not supplied"
    return str(search.get_album_tracks(album_id, premium=users_by_ip[request.remote_addr].is_premium))


def start():
    app.run(host=config.settings['rest_ip'], port=config.settings['rest_port'], use_reloader=False, debug=True)
