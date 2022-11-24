from flask import Blueprint, render_template, jsonify

help = Blueprint('profile', __name__)


@help.route('/a', methods=['GET'])
def routes_info():

    return 'a'