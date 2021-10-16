from flask import Blueprint, jsonify, request
from flask_cors import CORS
from ..utils.assets import get_balances, get_transactions, get_holdings
from ..utils.account import validate_auth_header

bp = Blueprint('api', __name__)
CORS(bp)

@bp.route('/api/balances', methods=(['GET']))
def get_assets_balances():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401
    
    user_data = validated_token[1]

    # get balances data(done via Assets)
    headers = {'yodlee_loginName':user_data[0]['yodlee_login_name'], 'nordigen_key': user_data[0]['nordigen_requisition']}
    response = jsonify(get_balances(headers))
    return response, 200


@bp.route('/api/transactions', methods=(['GET']))
def get_assets_transactions():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401
    
    user_data = validated_token[1]
    
    # get transactions data(done via Assets)
    headers = {'yodlee_loginName':user_data[0]['yodlee_login_name'], 'nordigen_key': user_data[0]['nordigen_requisition'],'binance_key':user_data[0]['binance_key'], 'binance_secret':user_data[0]['binance_secret'], 'coinbase_key': user_data[0]['coinbase_api_key'], 'coinbase_secret': user_data[0]['coinbase_api_secret']}
    response = jsonify(get_transactions(headers))
    return response, 200


@bp.route('/api/holdings', methods=(['GET']))
def get_assets_holdings():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401
    
    user_data = validated_token[1]
    
    # get holdings data(done via Assets)
    headers = {'yodlee_loginName':user_data[0]['yodlee_login_name'], 'binance_key':user_data[0]['binance_key'], 'binance_secret':user_data[0]['binance_secret'], 'coinbase_key': user_data[0]['coinbase_api_key'], 'coinbase_secret': user_data[0]['coinbase_api_secret']}
    response = jsonify(get_holdings(headers))
    return response, 200