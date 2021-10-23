import re
from flask import Blueprint, request, jsonify
import aiohttp, asyncio

from ..utils.yodlee_api import get_balances as get_yodlee_balances
from ..utils.yodlee_api import get_holdings as get_yodlee_holdings
from ..utils.yodlee_api import get_transactions as get_yodlee_transactions
from ..utils.nordigen import get_all_account_balances as get_nordigen_balances
from ..utils.nordigen import get_account_transactions as get_nordigen_transactions
from ..utils.binance_api import get_balances as get_binance_holdings
from ..utils.coinbase_api import get_account_balances as get_coinbase_holdings
from ..utils.custom_assets_api import get_holdings as get_custom_assets_holdings

bp = Blueprint('api', __name__)

@bp.route('/balances', methods=(['GET']))
async def get_balances():
    results = {}
    async with aiohttp.ClientSession() as session:
            tasks = []
            tasks.append(asyncio.ensure_future(get_yodlee_balances(request.headers.get('yodlee_loginName'), session=session)))
            tasks.append(asyncio.ensure_future(get_nordigen_balances(request.headers.get('nordigen_key'), session=session)))

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
        tasks.append(get_binance_holdings(request.headers.get('binance_key'), request.headers.get('binance_secret')))
        tasks.append(get_coinbase_holdings(request.headers.get('coinbase_key'), request.headers.get('coinbase_secret')))

        responses = await asyncio.gather(*tasks)
        results['yodlee'] = responses[0]
        results['custom_assets'] = responses[1]
        results['binance'] = responses[2]
        results['coinbase'] = responses[3]
    
    return jsonify(results)

@bp.route('/transactions', methods=(['GET']))
async def get_transactions():
    results = {}
    async with aiohttp.ClientSession() as session:
        tasks = []
        tasks.append(asyncio.ensure_future(get_yodlee_transactions(request.headers.get('yodlee_loginName'), session=session)))
        tasks.append(asyncio.ensure_future(get_nordigen_transactions(request.headers.get('nordigen_key'), session=session)))

        responses = await asyncio.gather(*tasks)
        results['yodlee'] = responses[0]
        results['nordigen'] = responses[1]
    
    return jsonify(results)