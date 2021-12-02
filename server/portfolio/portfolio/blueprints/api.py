import logging
import os
from datetime import datetime
import json
from threading import Thread

import requests
from flask import Blueprint, jsonify, request
from flask_cors import CORS
from ..utils.assets import get_balances, get_transactions, get_holdings, get_assets_recent_transactions
from ..utils.account import validate_auth_header
from ..utils.cache_assets import cache_assets
from ..utils.custom_assets import create_asset as create_custom_asset
from ..utils.format import group_balances, set_historical_balance

import aiohttp, asyncio

from ..utils.reference import convert_assets_to_base_currency_and_get_total_gbp, \
    convert_transactions_currency_to_base_currency

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
    internal = user_data.get('internal')
    if internal:
        user_data.pop('internal')
    nordigen_requisitions = json.dumps([x['requisition_id'] for x in user_data['nordigenrequisition_set']])

    balances_headers = {'yodlee_loginName': user_data['user_identifier'],
                        'nordigen_requisitions': nordigen_requisitions}
    holdings_headers = {'yodlee_loginName': user_data['user_identifier'],
                        "custom_assets_key": user_data['user_identifier'], 'binance_key': user_data['binance_key'],
                        'binance_secret': user_data['binance_secret'], 'coinbase_key': user_data['coinbase_api_key'],
                        'coinbase_secret': user_data['coinbase_api_secret']}

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(get_balances(headers=balances_headers, session=session)),
                 asyncio.ensure_future(get_holdings(headers=holdings_headers, session=session))]

        responses = await asyncio.gather(*tasks)

        balances = responses[0]
        holdings = responses[1]
        total_gbp = await convert_assets_to_base_currency_and_get_total_gbp(
            user_data['base_currency'],
            balances,
            holdings,
            session,
        )
        data = group_balances(balances, holdings)
        Thread(target=cache_assets, args=(total_gbp, user_data['user_identifier'])).start()
    if not internal:
        total_amount = total_gbp
        valid_data = {
            'balance': total_amount,
            'id': user_data['user_identifier']
        }
        url = os.environ.get('BALANCE_CACHING_SERVICE_URL')
        try:
            response = requests.post(url+'balances/add/', data=valid_data)
        except Exception as e:
            print('Connection to balance cashing service failed:'+str(e))
    return jsonify(data), 200


@bp.route('/api/transactions', methods=(['GET']))
async def get_account_transactions():
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
    response = get_transactions(headers)
    async with aiohttp.ClientSession() as session:
        await convert_transactions_currency_to_base_currency(user_data['base_currency'], response, session)
    return jsonify(response), 200


@bp.route('/api/recent-transactions', methods=(['GET']))
async def get_recent_transactions():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    recent = request.headers.get('Recent')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401

    user_data = validated_token[1]
    all_requisitions = user_data['nordigenrequisition_set']
    all_requisitions = json.dumps([el['requisition_id'] for el in all_requisitions])

    headers = {'yodlee_loginName': user_data['user_identifier'], 'nordigen_requisitions': all_requisitions,
               'coinbase_key': user_data['coinbase_api_key'], 'coinbase_secret': user_data['coinbase_api_secret']}

    response = get_assets_recent_transactions(headers=headers)
    if response:
        async with aiohttp.ClientSession() as session:
            await convert_transactions_currency_to_base_currency(
                user_data['base_currency'], response, session, recent=True
            )

        response['content'].sort(key=lambda x: datetime.strptime(list(x.values())[0]['date'], "%Y-%m-%d"), reverse=True)

        if recent == 'True':
            response = {"status": "success", "content": response["content"][:6]}
    else:
        response = None

    return jsonify(response)


@bp.route('/api/historical-balances', methods=(['GET']))
async def get_historical_balances():
    # check if a token was passed in the Authorization header
    received_token = request.headers.get('Authorization')
    validated_token = validate_auth_header(received_token)

    if not validated_token[0]:
        return jsonify(validated_token[1]), 401

    user_data = validated_token[1]
    all_requisitions = user_data['nordigenrequisition_set']
    all_requisitions = json.dumps([el['requisition_id'] for el in all_requisitions])
    balances_headers = {'yodlee_loginName': user_data['user_identifier'],
                        'nordigen_requisitions': all_requisitions}
    holdings_headers = {'yodlee_loginName': user_data['user_identifier'],
                        "custom_assets_key": user_data['user_identifier'], 'binance_key': user_data['binance_key'],
                        'binance_secret': user_data['binance_secret'], 'coinbase_key': user_data['coinbase_api_key'],
                        'coinbase_secret': user_data['coinbase_api_secret']}

    transactions_headers = {'yodlee_loginName': user_data['user_identifier'], 'nordigen_requisitions': all_requisitions,
                            'coinbase_key': user_data['coinbase_api_key'],
                            'coinbase_secret': user_data['coinbase_api_secret']}

    all_transactions = get_assets_recent_transactions(headers=transactions_headers)
    if all_transactions:
        async with aiohttp.ClientSession() as session:
            tasks = []
            tasks.append(asyncio.ensure_future(get_balances(headers=balances_headers, session=session)))
            tasks.append(asyncio.ensure_future(get_holdings(headers=holdings_headers, session=session)))
            tasks.append(asyncio.ensure_future(convert_transactions_currency_to_base_currency(
                user_data['base_currency'], all_transactions, session, recent=True
            )))

            responses = await asyncio.gather(*tasks)

            balances = responses[0]
            holdings = responses[1]
            await convert_assets_to_base_currency_and_get_total_gbp(
                user_data['base_currency'],
                balances,
                holdings,
                session,
            )
            total_balance = group_balances(balances, holdings)['total']

        all_transactions['content'].sort(key=lambda x: datetime.strptime(list(x.values())[0]['date'], "%Y-%m-%d"),
                                         reverse=True)

    historical_balances = set_historical_balance(total_balance, all_transactions['content'])
    if historical_balances:
        return jsonify(historical_balances)
    return jsonify("Error")


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

