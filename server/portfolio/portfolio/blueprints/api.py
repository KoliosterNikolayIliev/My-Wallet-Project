import json

from flask import Blueprint, jsonify, request
from flask_cors import CORS
from ..utils.assets import get_balances, get_transactions, get_holdings
from ..utils.account import validate_auth_header
from ..utils.custom_assets import create_asset as create_custom_asset
from ..utils.format import group_balances

import aiohttp, asyncio

bp = Blueprint('api', __name__)
CORS(bp)


@bp.route('/api/assets', methods=(['GET']))
async def get_assets():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401

    user_data = validated_token[1]
    nordigen_requisitions = json.dumps([x['requisition_id'] for x in user_data['nordigenrequisition_set']])

    balances_headers = {'yodlee_loginName': user_data['user_identifier'],
                        'nordigen_requisitions': nordigen_requisitions}
    holdings_headers = {'yodlee_loginName': user_data['user_identifier'], "custom_assets_key": user_data['user_identifier'],'binance_key': user_data['binance_key'],
                        'binance_secret': user_data['binance_secret'], 'coinbase_key': user_data['coinbase_api_key'],
                        'coinbase_secret': user_data['coinbase_api_secret']}

    results = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        tasks.append(asyncio.ensure_future(get_balances(headers=balances_headers, session=session)))
        tasks.append(asyncio.ensure_future(get_holdings(headers=holdings_headers, session=session)))

        responses = await asyncio.gather(*tasks)

        balances = responses[0]
        holdings = responses[1]

        data = group_balances(balances, holdings)


    return jsonify(data), 200


@bp.route('/api/transactions', methods=(['GET']))
def get_account_transactions():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401

    user_data = validated_token[1]

    # get transactions data(done via Assets)
    headers = {
        'provider': request.headers.get('provider'),
        'account': request.headers.get('account'),

        'yodlee_loginName': user_data['user_identifier'],
        'binance_key': user_data['binance_key'],
        'binance_secret': user_data['binance_secret'],

        'coinbase_key': user_data['coinbase_api_key'],
        'coinbase_secret': user_data['coinbase_api_secret']
    }
    response = jsonify(get_transactions(headers))
    return response, 200

@bp.route('/api/create-asset', methods=(['GET']))
def create_asset():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401

    user_data = validated_token[1]
    key = user_data['user_identifier']

    asset_type = request.headers.get('type')
    symbol = request.headers.get('symbol')
    amount = request.headers.get('amount')

    if asset_type not in ['crypto', 'stock']:
        return jsonify({'status': 'failed', 'content': 'Error: invalid asset type'}), 400
    try:
        response = create_custom_asset(key, asset_type, symbol, amount)
    except Exception as e:
        return jsonify({'status': 'failed', 'content': str(e)}), 400
    return jsonify(response), 200
    