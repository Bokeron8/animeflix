from core.apis import api
from flask import jsonify
from flask_restx import Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime
from .utils import search_anime, get_episodes, get_servers


anime = api.namespace('/', description='Monoschinos APIs')


search_parser = reqparse.RequestParser()
search_parser.add_argument('q', type=str, required=True)

anime_parser = reqparse.RequestParser()
anime_parser.add_argument('title', type=str, required=True)

server_parser = anime_parser.copy()
server_parser.add_argument('episode-number', type=int, required=True)

@anime.route('/search-anime')
class SearchAnimeApi(Resource):
    @anime.doc(parser=search_parser)
    def get(self):
        args = search_parser.parse_args()
        anime = search_anime(args.get('q'))
        return jsonify(anime)
    
@anime.route('/get-episodes')
class GetEpisodesApi(Resource):
    @anime.doc(parser=anime_parser)
    def get(self):
        args = anime_parser.parse_args()
        episodes = get_episodes(args.get('title'))
        return jsonify(episodes)

@anime.route('/get-servers')
class GetServersApi(Resource):
    @anime.doc(parser=server_parser)
    def get(self):
        args = server_parser.parse_args()
        title = args.get('title')
        episode_number = args.get('episode-number')
        servers = get_servers(title, episode_number)

        return jsonify(servers)