from flask import jsonify, redirect
from flask_restx import Resource, reqparse, Namespace
from .utils import search_anime, get_episodes, get_servers, get_last_episodes


anime_api = Namespace('/', description='Monoschinos APIs')

search_parser = reqparse.RequestParser()
search_parser.add_argument('q', type=str, required=True)

anime_parser = reqparse.RequestParser()
anime_parser.add_argument('title', type=str, required=True)

server_parser = anime_parser.copy()
server_parser.add_argument('episode-number', type=int, required=True)

@anime_api.route('/search')
class SearchAnimeApi(Resource):
    @anime_api.doc(parser=search_parser)
    def get(self):
        args = search_parser.parse_args()
        query = args.get('q')
        anime = search_anime(query)
        return jsonify(anime)
    
@anime_api.route('/get-episodes')
class GetEpisodesApi(Resource):
    @anime_api.doc(parser=anime_parser)
    def get(self):
        args = anime_parser.parse_args()
        episodes = get_episodes(args.get('title'))
        return jsonify(episodes)

@anime_api.route('/get-servers')
class GetServersApi(Resource):
    @anime_api.doc(parser=server_parser)
    def get(self):
        args = server_parser.parse_args()
        title = args.get('title')
        episode_number = args.get('episode-number')
        servers = get_servers(title, episode_number)

        return jsonify(servers)

@anime_api.route('/get-last-episodes')
class GetLastEpisodesApi(Resource):
    @anime_api.doc()
    def get(self):
        last_episodes = get_last_episodes()

        return jsonify(last_episodes)

