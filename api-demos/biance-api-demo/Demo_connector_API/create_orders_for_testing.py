import logging

from binance.error import ClientError

from Demo_connector_API.decorators import require_auth
from testnet_setup import SPOT_CLIENT, DEBUG

@require_auth
def make_order(symbol="BTCBUSD", client=SPOT_CLIENT):

    params = {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": 0.002,
        "price": 9500,
    }

    try:
        response = client.new_order(**params)
        if DEBUG:
            logging.info(response)
        return response
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
