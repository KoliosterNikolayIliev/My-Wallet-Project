import logging
import time

from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient

from testnet_setup import SPOT_CLIENT


def get_live_account_data(client=SPOT_CLIENT):
    config_logging(logging, logging.DEBUG)

    def message_handler(message):
        print(message)

    response = client.new_listen_key()

    logging.info("Receving listen key : {}".format(response["listenKey"]))

    ws_client = SpotWebsocketClient(stream_url="wss://testnet.binance.vision")
    ws_client.start()

    ws_client.user_data(
        listen_key=response["listenKey"],
        id=1,
        callback=message_handler,
    )

    time.sleep(30)

    logging.debug("closing ws connection")
    ws_client.stop()


def get_live_combined_data():
    config_logging(logging, logging.DEBUG)

    def message_handler(message):
        logging.info(message)

    my_client = SpotWebsocketClient()
    my_client.start()

    # subscribe one stream
    my_client.instant_subscribe(
        stream="bnbusdt@bookTicker",
        callback=message_handler,
    )

    time.sleep(3)

    # subscribe multiple streams
    my_client.instant_subscribe(
        stream=["bnbusdt@bookTicker", "ethusdt@bookTicker"],
        callback=message_handler,
    )

    time.sleep(30)

    logging.debug("closing ws connection")
    my_client.stop()


def get_live_trade_data():
    config_logging(logging, logging.DEBUG)

    def message_handler(message):
        print(message)

    my_client = SpotWebsocketClient()
    my_client.start()

    my_client.trade(
        symbol="bnbusdt",
        interval="1m",
        id=1,
        callback=message_handler,
    )

    time.sleep(2)

    my_client.trade(
        symbol="eosusdt",
        interval="1m",
        id=2,
        callback=message_handler,
    )

    time.sleep(30)

    logging.debug("closing ws connection")
    my_client.stop()


def test_live_data():
    config_logging(logging, logging.DEBUG)

    def message_handler(message):
        print(message)

    my_client = SpotWebsocketClient()
    my_client.start()

    my_client.agg_trade(
        symbol="btcusdt",
        id=1,
        callback=message_handler,
    )

    time.sleep(1)

    my_client.agg_trade(
        symbol="bnbusdt",
        id=2,
        callback=message_handler,
    )

    time.sleep(10)

    logging.debug("closing ws connection")
    my_client.stop()
