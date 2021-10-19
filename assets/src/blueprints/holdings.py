from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import binance_api, yodlee_api, coinbase_api, custom_assets_api


holdings = Blueprint('holdings', __name__)
api = Api(holdings)


class GetHoldings(Resource):
    def get(self):
        data = {
            'yodlee': yodlee_api.get_holdings(request.headers.get('yodlee_loginName')),
            'binance': binance_api.get_balances(request.headers.get('binance_key'), request.headers.get('binance_secret')),
            'coinbase': coinbase_api.get_account_balances(request.headers.get('coinbase_key'), request.headers.get('coinbase_secret')),
            'custom_assets': custom_assets_api.get_holdings(request.headers.get('custom_assets_key'))
        }

        return data


api.add_resource(GetHoldings, '/')
 