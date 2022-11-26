<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
#from decouple import config
from .apis import blueprint as api
from core.views.routes_help import anime

def create_app():
    app = Flask(__name__)
    
    #app.config.from_object(config("APP_SETTINGS"))
    app.register_blueprint(api)
    app.register_blueprint(anime)

    return app
