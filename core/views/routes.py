from flask import Blueprint, render_template, jsonify, url_for, request, send_from_directory, redirect
import os
import requests

anime = Blueprint('anime', __name__)

@anime.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(anime.root_path, 'static'),
                            'favicon.ico', mimetype='image/vnd.microsoft.icon')

@anime.route('/', methods=['GET'])
def index():
    url = request.host_url + url_for('api./_get_last_episodes_api')
    r = requests.get(url)

    last_episodes = r.json()
    return render_template("index.html", last_episodes=last_episodes)

@anime.route('/search', methods=['GET'])
def search():
    args = request.args
    url = request.host_url + 'api/v1'

    r = requests.get(f'{url}/search', params=args)
    animes = r.json()
    
    return render_template("search.html", animes=animes)
    

@anime.route('/<anime_name>', methods=['GET'])
def episodes(anime_name):
    url = request.host_url + 'api/v1'
    params = {'title': anime_name}
    r = requests.get(f'{url}/get-episodes', params=params)
    episodes = r.json()
    return render_template("anime.html", episodes=episodes, anime=anime_name)

@anime.route('/<anime_name>/<episode_number>', methods=['GET'])
def watch(anime_name, episode_number):
    url = request.host_url + 'api/v1'
    params = {'title': anime_name, 'episode-number': episode_number}
    r = requests.get(f'{url}/get-episode-info', params=params)
    json_data = r.json()
    servers = json_data['servers']
    anime_name = json_data['title']
    return render_template("watch.html", servers=servers, anime_name=anime_name)

@anime.route('/series')
def series():
    return 'Series'

@anime.route('/peliculas')
def peliculas():
    return 'Peliculas'

@anime.route('/novedades')
def novedades():
    return 'novedades'

@anime.route('/lista')
def lista():
    return 'lista'

@anime.route('/emision')
def emision():
    return 'emision'

@anime.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', e=e), 404
