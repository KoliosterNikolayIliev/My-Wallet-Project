from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import nordigen


balances = Blueprint('balances', __name__)
api = Api(balances)


class GetBalances(Resource):
    def get(self):
        data = {}
        nordigen_key = request.headers.get('nordigen')

        if nordigen_key:
            accounts = nordigen.list_accounts(nordigen_key).get('accounts')
            if not accounts:
                data['nordigen'] = 'No bank accounts'

            else:
                data['nordigen'] = {}

                for account in accounts:
                    data['nordigen'][account] = nordigen.get_account_balances(account).get('balances')[0]

        return data


api.add_resource(GetBalances, '/')
