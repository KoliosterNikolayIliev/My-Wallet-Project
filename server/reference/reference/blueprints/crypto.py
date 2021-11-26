from flask import (Blueprint, jsonify, current_app)
from ..third_party_apis.coinlayer_api import CoinlayerApi

# create blueprint
bp = Blueprint('crypto', __name__, url_prefix='/crypto')

# microservice endpoint to return the latest prices for crypto
@bp.route('/prices', methods=(['GET']))
def prices():
    """
    ---
    get:
      description: Request latest price data for available cryptocurrencies
      responses:
        '200':
          description: A successful call was made and the results were returned
          content:
            application/json:
              schema: OutputSchema
              example:
                ADA: 2.314212
                BTC: 47039.2419
    """
    instance: Crypto = current_app.config["CRYPTO"]
    return instance.handle_prices_request()

class Crypto():
    def __init__(self, coinlayer_api: CoinlayerApi, scheduler):
        self.coinlayer_api = coinlayer_api
        # store latest prices for crypto
        self.crypto_prices_store = {}

        # fetch price data for crypto the first time the server goes live
        scheduler.add_job(\
                func=self.update_prices,\
                id='crypto_price_update',\
                max_instances=1\
        )

        # fetch price data for crypto every 24 hours
        scheduler.add_job(\
                func=self.update_prices,\
                trigger='interval',\
                seconds=86400,\
                id='periodic_crypto_price_update'
        )

    def update_prices(self):
        self.crypto_prices_store = self.coinlayer_api.fetch_crypto_price_data()

    def handle_prices_request(self):
        if not self.crypto_prices_store:
            self.update_prices()
        return jsonify(self.crypto_prices_store)
