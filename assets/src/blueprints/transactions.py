from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import nordigen, yodlee_api, coinbase_api


transactions = Blueprint('transactions', __name__)
api = Api(transactions)


class GetTransactions(Resource):
    def get(self):
        data = {
            'nordigen': nordigen.get_account_transactions(request.headers.get('nordigen_key')),
            'yodlee': yodlee_api.get_transactions(request.headers.get('yodlee_loginName')),
            'coinbase': coinbase_api.get_transactions(request.headers.get('coinbase_key'), request.headers.get('coinbase_secret'))
        }

        return data


api.add_resource(GetTransactions, '/')
