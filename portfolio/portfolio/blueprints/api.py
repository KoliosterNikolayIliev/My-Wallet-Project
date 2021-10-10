from flask import Blueprint, jsonify, request
from flask_cors import CORS
from ..utils.assets import get_balances, get_transactions
from ..utils.account import validate_token

bp = Blueprint('api', __name__)
CORS(bp)

@bp.route('/api/balances', methods=(['GET']))
def get_assets_balances():
    # check if a token was passed in the Authorization header
    token = request.headers.get('Authorization')
    
    if not token:
        response = jsonify({'error': 'No token provided'})
        return response, 401
    
    # check if the token is valid(done via Account)
    user_data = validate_token(token)
    if not user_data:
        response = jsonify({'error': 'Invalid token'})
        return response, 401

    # get balances data(done via Assets)
    headers = {'yodlee_loginName':user_data[0]['yodlee_login_name'], 'binance_key':user_data[0]['binance_key'], 'binance_secret':user_data[0]['binance_secret']}
    response = jsonify(get_balances(headers))
    return response, 200


@bp.route('/api/transactions', methods=(['GET']))
def get_assets_transactions():
    # check if a token was passed in the Authorization header
    token = request.headers.get('Authorization')
    
    if not token:
        response = jsonify({'error': 'No token provided'})
        return response, 401
    
    # check if the token is valid(done via Account)
    user_data = validate_token(token)
    if not user_data:
        response = jsonify({'error': 'Invalid token'})
        return response, 401
    
    # get transactions data(done via Assets)
    headers = {'yodlee_loginName':user_data[0]['yodlee_login_name'], 'binance_key':user_data[0]['binance_key'], 'binance_secret':user_data[0]['binance_secret']}
    response = jsonify(get_transactions(headers))
    return response, 200