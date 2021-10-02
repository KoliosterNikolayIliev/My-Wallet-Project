from flask import (Blueprint, jsonify)
import os, requests
from .extensions import scheduler

# store latest prices for crypto
crypto_prices_store = {}

# create blueprint
bp = Blueprint('crypto', __name__, url_prefix='/crypto')

def fetch_crypto_price_data():
    global crypto_prices_store
    req = requests.get('http://api.coinlayer.com/live', params={'access_key': os.environ['CL_API_KEY']})
    res = req.json()

     # if there is an error, print the error message, else update the crypto_prices_store
    try:
        res_body = res['rates']
        for res_key, res_value in res_body.items():
            crypto_prices_store[res_key] = res_value
    except:
        print(f"Error: {req['error']['info']}")
    

# fetch price data for crypto the first time the server goes live
scheduler.add_job(func=fetch_crypto_price_data, id='crypto_price_update', max_instances=1)

# fetch price data for crypto every 24 hours
scheduler.add_job(func=fetch_crypto_price_data, trigger='interval', seconds=86400, id='periodic_crypto_price_update')

# microservice endpoint to return the latest prices for crypto
@bp.route('/prices', methods=(['GET']))
def prices():
    if crypto_prices_store:
        return jsonify(crypto_prices_store)
    fetch_crypto_price_data()
    return jsonify(crypto_prices_store)
