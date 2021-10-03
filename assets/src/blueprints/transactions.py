from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import nordigen

transactions = Blueprint('transactions', __name__)
api = Api(transactions)


class GetTransactions(Resource):
    def get(self):
        data = {}
        nordigen_key = request.form.get('nordigen')

        if nordigen_key:
            accounts = nordigen.list_accounts(nordigen_key).get('accounts')

            if not accounts:
                data['nordigen'] = 'No bank accounts'

            else:
                data['nordigen'] = {}

                for account in accounts:
                    data['nordigen'][account] = nordigen.get_account_transactions(account)

        return data


api.add_resource(GetTransactions, '/')
