from flask import request, Blueprint
from flask_restful import Resource, Api
from utils import nordigen


balances = Blueprint('balances', __name__)
api = Api(balances)


class GetBalances(Resource):
    def get(self):
        data = {
            'nordigen': nordigen.get_account_balances(request.headers.get('nordigen')),
        }

        return data


api.add_resource(GetBalances, '/')
