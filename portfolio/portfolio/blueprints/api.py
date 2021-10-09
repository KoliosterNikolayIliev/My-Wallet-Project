from flask import Blueprint, jsonify, request
from ..utils.assets import get_balances, get_transactions

bp = Blueprint('api', __name__)

@bp.route('/balances', methods=(['GET']))
def get_assets_balances():
    headers = None # this data will be received from Account(keys, etc.)
    return jsonify(get_balances(headers))


@bp.route('/transactions', methods=(['GET']))
def get_assets_transactions():
    headers = None # this data will be received from Account(keys, etc.)
    return jsonify(get_transactions(headers))