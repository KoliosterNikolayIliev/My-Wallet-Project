from flask import (Blueprint, jsonify)
import os, requests
from ..utils.extensions import scheduler

# shortlisted stocks
STOCKS_LIST = ["AMZN", "MSFT", "GOOGL", "AMD", "MRNA", "TSLA", "PLTR", "AAPL"]

MOCK_ENVIRONMENT = os.environ.get('MOCK_ENVIRONMENT')

# store latest prices for shortlisted stocks
stocks_prices_store = {}

# create blueprint
bp = Blueprint('stocks', __name__, url_prefix='/stocks')

# fetch real-time price data for shortlisted stocks
def fetch_stocks_price_data(symbols: list):
    global stocks_prices_store
    if not MOCK_ENVIRONMENT == "True":
      symbols = (',').join(symbols)
      req = requests.get('https://api.twelvedata.com/price', params={'symbol': symbols, 'apikey': os.environ['TD_API_KEY'], 'interval': '1min'})
      res = req.json()

      # if there is an error, print the error message, else update the stocks_prices_store
      try:
          for res_key, res_value in res.items():
              stocks_prices_store[res_key] = res_value['price']
      except:
          print(f"Error: {res['message']}")
    else:
      stocks_prices_store = {
        'AAPL': 138.13,
        'MSFT': 281.24,
        'PLTR': 23.20,
        'GOOGL': 2654.24,
        'AMZN': 3185.66,
        'MRNA': 325.30,
        'TSLA': 782.06,
        'AMD': 100.00,
    }
  
        

# fetch price data for shortlisted stocks the first time the server goes live
scheduler.add_job(func=fetch_stocks_price_data, args=[STOCKS_LIST], id='stocks_price_update', max_instances=1)

# fetch price data for shortlisted stocks every 24 hours
scheduler.add_job(func=fetch_stocks_price_data, args=[STOCKS_LIST], trigger='interval', seconds=86400, id='periodic_stocks_price_update')

# microservice endpoint to return the latest prices for shortlisted stocks
@bp.route('/prices', methods=(['GET']))
def prices():
    """
    ---
    get:
      description: Request latest price data for available stocks
      responses:
        '200':
          description: A successful call was made and the results were returned
          content:
            application/json:
              schema: OutputSchema
              example:
                AAPL: 142.64999
                AMD: 102.45000
    """
    if stocks_prices_store:
        return jsonify(stocks_prices_store)
    fetch_stocks_price_data(STOCKS_LIST)
    return jsonify(stocks_prices_store)
