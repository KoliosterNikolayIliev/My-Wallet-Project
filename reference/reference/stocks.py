from flask import (Blueprint, jsonify)
import os, requests
from .extensions import scheduler

# shortlisted stocks
STOCKS_LIST = ["AMZN", "MSFT", "GOOGL", "AMD", "MRNA", "TSLA", "PLTR", "AAPL"]

# store latest prices for shortlisted stocks
prices_store = {}

# create blueprint
bp = Blueprint('stocks', __name__, url_prefix='/stocks')

# fetch real-time price data for shortlisted stocks
def fetch_price_data(symbols: list):
    global prices_store
    symbols = (',').join(symbols)
    req = requests.get('https://api.twelvedata.com/price', params={'symbol': symbols, 'apikey': os.environ['TD_API_KEY'], 'interval': '1min'})
    req = req.json()

    # if there is an error, print the error message, else update the prices_store
    try:
        for res_key, res_value in req.items():
            prices_store[res_key] = res_value['price']
    except:
        print(f"Error: {req['message']}")
        

# fetch price data for shortlisted stocks the first time the server goes live
scheduler.add_job(func=fetch_price_data, args=[STOCKS_LIST], id='price_update', max_instances=1)

# fetch price data for shortlisted stocks every 24 hours
scheduler.add_job(func=fetch_price_data, args=[STOCKS_LIST], trigger='interval', seconds=86400, id='periodic_price_update')

# microservice endpoint to return the latest prices for shortlisted stocks
@bp.route('/prices', methods=(['GET']))
def prices():
    if prices_store:
        return jsonify(prices_store)
    fetch_price_data(STOCKS_LIST)
    return jsonify(prices_store)
