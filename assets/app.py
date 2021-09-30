from flask import Flask, request
from flask_restful import Resource, Api
import nordigen
import uuid

app = Flask(__name__)
api = Api(app)


class LinkBankAccount(Resource):
    def get(self):
        return nordigen.get_banks_by_country('GB'), 200

    def post(self):
        requisition_id = request.form.get('requisition_id')
        user_id = request.form.get('user_id')
        aspsp_id = request.form.get('aspsp_id')

        if not requisition_id:
            requisition_id = nordigen.create_requisition(
                uuid.uuid1(), user_id, 'https://3vial.io', []
            ).get('id')

            if not requisition_id:
                return {'detail': 'Client Reference: already exists', 'status_code': 400}, 400

        return {'requisition_id': requisition_id, 'auth_link': nordigen.build_link(requisition_id, aspsp_id)}


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


api.add_resource(LinkBankAccount, '/api/link-account/nordigen')
api.add_resource(GetUserAssets, '/api/user-assets')

if __name__ == '__main__':
    app.run()
