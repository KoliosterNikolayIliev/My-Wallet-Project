import json
import os
from flask import Blueprint, request, jsonify
import aiohttp, asyncio, httpx

from ..utils.yodlee_api import get_balances as get_yodlee_balances
from ..utils.yodlee_api import get_holdings as get_yodlee_holdings
from ..utils.yodlee_api import get_transactions as get_yodlee_transactions
from ..utils.yodlee_api import get_all_transactions as get_all_yodlee_transactions
from ..utils.nordigen import get_all_accounts_balances as get_nordigen_balances
from ..utils.nordigen import get_account_transactions as get_nordigen_transactions
from ..utils.nordigen import get_all_transactions as get_all_nordigen_transactions
from ..utils.nordigen import get_single_account_balance as get_nordigen_balance
from ..utils.binance_api import get_balances as get_binance_holdings
from ..utils.coinbase_api import get_account_balances as get_coinbase_holdings
from ..utils.coinbase_api import get_transactions as get_coinbase_transactions
from ..utils.coinbase_api import get_all_transactions as get_all_coinbase_transactions
from ..utils.custom_assets_api import get_holdings as get_custom_assets_holdings

bp = Blueprint('api', __name__)

@bp.route('/balances', methods=(['GET']))
async def get_balances():
    results = {}
    nordigen_requisitions = request.headers.get('nordigen_requisitions')
    nordigen_requisitions = json.loads(nordigen_requisitions) if nordigen_requisitions else []
    async with aiohttp.ClientSession() as session:
        tasks = (
            asyncio.ensure_future(get_yodlee_balances(request.headers.get('yodlee_loginName'), session=session)),
            asyncio.ensure_future(get_nordigen_balances(nordigen_requisitions, session=session)),
        )

        responses = await asyncio.gather(*tasks)
        results['yodlee'] = responses[0]
        results['nordigen'] = responses[1]

    return jsonify(results)

@bp.route('/holdings', methods=(['GET']))
async def get_holdings():
    results = {}
    async with aiohttp.ClientSession() as session:
        tasks = []
        tasks.append(asyncio.ensure_future(get_yodlee_holdings(request.headers.get('yodlee_loginName'), session=session)))
        tasks.append(asyncio.ensure_future(get_custom_assets_holdings(request.headers.get('custom_assets_key'), session=session)))
        tasks.append(asyncio.ensure_future(get_binance_holdings(request.headers.get('binance_key'), request.headers.get('binance_secret'), session=session)))
        tasks.append(get_coinbase_holdings(request.headers.get('coinbase_key'), request.headers.get('coinbase_secret')))

        responses = await asyncio.gather(*tasks)
        results['yodlee'] = responses[0]
        results['custom_assets'] = responses[1]
        results['binance'] = responses[2]
        results['coinbase'] = responses[3]

    return jsonify(results)

@bp.route('/transactions', methods=(['GET']))
async def get_transactions():
    async with aiohttp.ClientSession() as session:
        if request.headers.get('provider') == 'nordigen':
            results = await get_nordigen_transactions(request.headers.get('account'), session)

        elif request.headers.get('provider') == 'yodlee':
            results = await get_yodlee_transactions(request.headers.get('yodlee_loginName'), session, request.headers.get('account'))

        elif request.headers.get('provider') == 'coinbase':
            results = await get_coinbase_transactions(request.headers.get('coinbase_key'),
                                                      request.headers.get('coinbase_secret'),
                                                      request.headers.get('account'))

        else:
            return {'status': 'failed', 'content': 'provider is not valid or missing'}

    return jsonify(results)

@bp.route('/recent-transactions', methods=(['GET']))
async def get_recent_transactions():
    nordigen_requisitions = json.loads(request.headers.get('nordigen_requisitions'))
    yodlee_login_name = request.headers.get('yodlee_loginName')
    coinbase_key = request.headers.get('coinbase_key')
    coinbase_secret = request.headers.get('coinbase_secret')

    result = []
    final = []

    if nordigen_requisitions or yodlee_login_name or (coinbase_secret and coinbase_key):
        try:
            async with aiohttp.ClientSession() as session:
                tasks = []
                if yodlee_login_name:
                    tasks.append(asyncio.ensure_future(get_all_yodlee_transactions(yodlee_login_name, session=session)))
                if nordigen_requisitions:
                    await get_all_nordigen_transactions(requisitions=nordigen_requisitions, session=session, tasks=tasks)

                responses = await asyncio.gather(*tasks)
                for response in responses:
                    if type(response) is dict:
                        if not response.get('status') == "failed":
                            transactions = response.get('content')
                            for source in transactions:
                                for transaction in source:
                                    result.append(transaction)
                        else:
                            continue
                    result.append(response)
            
            coinbase_tasks = []
            if coinbase_secret and coinbase_key:
                async with httpx.AsyncClient() as client:
                    await get_all_coinbase_transactions(coinbase_key, coinbase_secret, coinbase_tasks, client)
                    
                    coinbase_transactions = await asyncio.gather(*coinbase_tasks)

                    if coinbase_transactions:
                        for account in coinbase_transactions:
                            for transaction in account:
                                result.append(transaction)
            
            for element in result:
                if type(element) is list:
                    for transaction in element:
                        final.append(transaction)
                elif type(element) is dict:
                    final.append(element)

        except Exception as e:
            print(str(e))
            return None
        
        return jsonify({'status': 'success', 'content': final}) 
    else: 
        return None
