from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import nordigen

transactions = Blueprint('transactions', __name__)
api = Api(transactions)


class GetTransactions(Resource):
    def get(self):
        data = {
            'nordigen': nordigen.get_account_transactions(request.headers.get('nordigen'))
        }

        return data


api.add_resource(GetTransactions, '/')
