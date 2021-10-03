import uuid

from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import nordigen

link_accounts_api = Blueprint('api', __name__)
api = Api(link_accounts_api)


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


api.add_resource(LinkBankAccount, '/nordigen')
