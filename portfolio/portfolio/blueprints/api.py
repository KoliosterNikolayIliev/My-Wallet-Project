from flask import Blueprint, jsonify, request
from flask_cors import CORS
from ..utils.assets import get_balances, get_transactions
from ..utils.account import validate_token

bp = Blueprint('api', __name__)
CORS(bp)

@bp.route('/api/balances', methods=(['GET']))
def get_assets_balances():
    token = request.headers.get('Authorization')
    
    if not token:
        response = jsonify({'error': 'No token provided'})
        return response, 401
    
    user_data = validate_token(token)
    if not user_data:
        response = jsonify({'error': 'Invalid token'})
        return response, 401

    headers = {'yodlee_loginName':user_data[0]['yodlee_login_name'], 'binance_key':user_data[0]['binance_key'], 'binance_secret':user_data[0]['binance_secret']}
    response = jsonify(get_balances(headers))
    return response, 200


@bp.route('/transactions', methods=(['GET']), strict_slashes=False)
def get_assets_transactions():
    headers = None # this data will be received from Account(keys, etc.)
    return jsonify(get_transactions(headers))