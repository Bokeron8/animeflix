from core.apis import api
from flask import jsonify
from flask_restx import Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime


anime = api.namespace('/', description='Monoschinos APIs')


@anime.route('/get-horoscope/daily')
class DailyHoroscopeAPI(Resource):
    @anime.doc()
    def get(self):
        return 1