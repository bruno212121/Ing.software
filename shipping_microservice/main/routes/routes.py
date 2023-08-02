from flask import request, jsonify, json, Blueprint
import requests

shipping=Blueprint('shipping', __name__,url_prefix='/shipping')

@shipping.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'ok'}), 200 