from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    version='1.0',
    title='Monoschinos API',
    description='Get anime data easily',
    license='MIT',
    doc='/api/v1',
    prefix='/api/v1'
)

from .routes import anime
api.add_namespace(anime, path="/cat")