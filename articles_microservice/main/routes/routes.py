from flask import request, jsonify, json, Blueprint
import requests

articles=Blueprint('articles', __name__,url_prefix='/articles')

@articles.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'ok'}), 200 