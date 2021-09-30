from flask import (Blueprint, jsonify)
import os, json, requests

# create blueprint
bp = Blueprint('stocks', __name__, url_prefix='/stocks')

# store latest prices for shortlisted stocks
prices_store = {}

# fetch real-time price data for shortlisted stocks
def fetch_price_data(symbols):
    global prices_store
    symbols = (',').join(symbols)
    req = requests.get('https://api.twelvedata.com/price', params={'symbol': symbols, 'apikey': os.environ['TD_API_KEY'], 'interval': '1min'})
    req = req.json()
    for res_key, res_value in req.items():
        prices_store[res_key] = res_value['price']

fetch_price_data(["AAPL", "IBM"])

# microservice endpoint
@bp.route('/prices', methods=('GET'))
def prices():
    if prices_store:
        return jsonify(prices_store)
    fetch_price_data(["AAPL", "IBM"])
    return jsonify(prices_store)

