from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import binance_api, yodlee, coinbase_api


holdings = Blueprint('holdings', __name__)
api = Api(holdings)


class GetHoldings(Resource):
    def get(self):
        data = {
            'yodlee': yodlee.get_holdings(request.headers.get('yodlee_loginName')),
            'binance': binance_api.get_balances(request.headers.get('binance_key'), request.headers.get('binance_secret')),
            'coinbase': coinbase_api.get_account_balances(request.headers.get('coinbase_key'), request.headers.get('coinbase_secret'))
        }

        return data


api.add_resource(GetHoldings, '/')
 