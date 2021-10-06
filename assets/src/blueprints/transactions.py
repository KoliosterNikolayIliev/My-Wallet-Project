from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import nordigen, yodlee

transactions = Blueprint('transactions', __name__)
api = Api(transactions)


class GetTransactions(Resource):
    def get(self):
        data = {
            'nordigen': nordigen.get_account_transactions(request.headers.get('nordigen')),
            'yodlee': yodlee.get_transactions(request.headers.get('yodlee_loginName'))
        }

        return data


api.add_resource(GetTransactions, '/')
