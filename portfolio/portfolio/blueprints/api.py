from flask import Blueprint, jsonify, request
from flask_cors import CORS
from ..utils.assets import get_balances, get_transactions, get_holdings
from ..utils.account import validate_auth_header

bp = Blueprint('api', __name__)
CORS(bp)

    # headers = {'yodlee_loginName':user_data['yodlee_login_name'], 'nordigen_key': user_data['nordigen_requisition']}
    # response = jsonify(get_balances(headers))
    # return response, 200

    # headers = {'yodlee_loginName':user_data[0]['yodlee_login_name'], 'binance_key':user_data[0]['binance_key'], 'binance_secret':user_data[0]['binance_secret'], 'coinbase_key': user_data[0]['coinbase_api_key'], 'coinbase_secret': user_data[0]['coinbase_api_secret']}
    # response = jsonify(get_holdings(headers))


@bp.route('/api/assets', methods=(['GET']))
async def get_assets():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401
    
    user_data = validated_token[1]

    balances_headers = {'yodlee_loginName':user_data['yodlee_login_name'], 'nordigen_key': user_data['nordigen_requisition']}
    holdings_headers = {'yodlee_loginName':user_data['yodlee_login_name'], 'binance_key':user_data['binance_key'], 'binance_secret':user_data['binance_secret'], 'coinbase_key': user_data['coinbase_api_key'], 'coinbase_secret': user_data['coinbase_api_secret']}

    balances_response = await get_balances(balances_headers)
    holdings_response = await get_holdings(holdings_headers)

    response = {'balances': balances_response, 'holdings': holdings_response}
    return jsonify(response), 200

@bp.route('/api/transactions', methods=(['GET']))
def get_assets_transactions():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401
    
    user_data = validated_token[1]
    
    # get transactions data(done via Assets)
    headers = {'yodlee_loginName':user_data['yodlee_login_name'], 'nordigen_key': user_data['nordigen_requisition'],'binance_key':user_data['binance_key'], 'binance_secret':user_data['binance_secret'], 'coinbase_key': user_data['coinbase_api_key'], 'coinbase_secret': user_data['coinbase_api_secret']}
    response = jsonify(get_transactions(headers))
    return response, 200
