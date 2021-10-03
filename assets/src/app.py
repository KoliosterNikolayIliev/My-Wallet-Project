from flask import Flask, request
from flask_restful import Resource, Api
from utils import nordigen
from src.blueprints.link_accounts import link_accounts_api

app = Flask(__name__)
api = Api(app)


class GetUserAssets(Resource):
    def get(self):
        data = {}

        if request.form.get('nordigen'):
            accounts = nordigen.list_accounts(request.form['nordigen']).get('accounts')
            print(nordigen.list_accounts(request.form['nordigen']))

            if not accounts:
                return {'detail': 'Wrong requisition id', 'status_code': 400}, 400

            data['nordigen'] = []

            if accounts:
                for account in accounts:
                    account_data = {}
                    bank_metadata = nordigen.get_bank_by_id(nordigen.get_account_metadata(account)['aspsp_identifier'])
                    account_data['bank_name'] = bank_metadata['name']
                    account_data['bank_logo'] = bank_metadata['logo']
                    data['nordigen'].append(account_data)

            else:
                data['nordigen'] = 'No linked bank accounts'

        return data


api.add_resource(GetUserAssets, '/user-assets')
app.register_blueprint(link_accounts_api, url_prefix='/link-accounts')
