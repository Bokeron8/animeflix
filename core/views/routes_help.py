from flask import Blueprint, render_template, jsonify, url_for, request
import requests

anime = Blueprint('anime', __name__)


@anime.route('/search', methods=['GET'])
def search_anime():
    args = request.args
    query = args.get('q')
    url = request.host_url + 'api/v1'

    params = {'q': query}
    r = requests.get(f'{url}/search', params=params)
    return r.content

@anime.route('/<anime_name>', methods=['GET'])
def anime_episodes(anime_name):
    url = request.host_url + 'api/v1'
    
    params = {'title': anime_name}
    r = requests.get(f'{url}/get-episodes', params=params)
    return r.content

@anime.route('/<anime_name>/<episode_number>', methods=['GET'])
def watch_anime(anime_name, episode_number):
    url = request.host_url + 'api/v1'
    
    params = {'title': anime_name, 'episode-number': episode_number}
    r = requests.get(f'{url}/get-servers', params=params)
    return r.content