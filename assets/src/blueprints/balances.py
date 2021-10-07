from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import nordigen, yodlee, binance_api


balances = Blueprint('balances', __name__)
api = Api(balances)


class GetBalances(Resource):
    def get(self):
        data = {
            'nordigen': nordigen.get_account_balances(request.headers.get('nordigen')),
            'yodlee': yodlee.get_balances(request.headers.get('yodlee_loginName')),
            'binance': binance_api.get_balances(request.headers.get('binance_key'), request.headers.get('binance_secret')),
        }

        return data


api.add_resource(GetBalances, '/')
