import os

from flask import Blueprint, jsonify, request
import requests

bp = Blueprint('currencies', __name__, url_prefix='/currencies')


@bp.route('/prices', methods=['GET'])
def prices():
    """
        ---
        get:
          description: Get the latest foreign exchange reference rates for base currency given
          responses:
            '200':
              description: A successful call was made and the results were returned
              content:
                application/json:
                  schema: OutputSchema
                  example:
                    "AED": 4.279261,
                    "AFN": 104.246359,
                    "ALL": 121.542845,
        """
    base = request.headers.get('base')

    if not base:
        return jsonify({'Error': 'base currency was not provided'})

    response = requests.get('https://api.exchangerate.host/latest/', params={'base': base}).json()

    if response['base'].lower() != base.lower():
        return jsonify({'Error': 'symbol not found'}), 400

    return jsonify(response['rates']), 200
