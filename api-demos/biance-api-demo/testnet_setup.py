"""
KEYS are for testnet ONLY !!! All users registering on the Spot Test Network
automatically receive a balance in many different assets.

How to generate keys:
.....
How to use env variables:
    - Linux/Mac Terminal:
    export binance_api="your_api_key here in the double quotes"
    export binance_secret="your_api_secret_here here in the double quotes"

    - Windows CMD:

    set binance_api=your_api_key_here
    set binance_secret=your_api_secret_here

    - IDE environment variables - depend on the id (Pycharm{name:value})

    key examples(not real):

    key = "hGLWWbEWRKMLyy5gvo8dbwuufQmgJR88T9QBbWCfwGDO0chT3R1W3znALa18kT6B"
    secret = "qgve977nbhLuuTjobjkcCUy2WiAcCodgW7GZI8PBYWJRwk33ZbrmRVLouEKkmyEK"
"""

import os

from binance.spot import Spot as Client
import logging
from binance.lib.utils import config_logging

KEY = os.environ.get('binance_api')
SECRET = os.environ.get('binance_secret')
# for real API base_url=https://api.binance.com/api
SPOT_CLIENT = Client(key=KEY, secret=SECRET, base_url="https://testnet.binance.vision")
# make DEBUG False if functions need to return JSon data otherwise data will be printed in the console.

DEBUG = True
if DEBUG:
    config_logging(logging, logging.DEBUG)

more_info = logging.info

# Used only as a reference. In future can be refactored and used in the code.
SYMBOLS = {
    "BNBBUSD": "BNBBUSD",
    "BTCBUSD": "BTCBUSD",
    "ETHBUSD": "ETHBUSD",
    "LTCBUSD": "LTCBUSD",
    "TRXBUSD": "TRXBUSD",
    "XRPBUSD": "XRPBUSD",
    "BNBUSDT": "BNBUSDT",
    "BTCUSDT": "BTCUSDT",
    "ETHUSDT": "ETHUSDT",
    "LTCUSDT": "LTCUSDT",
    "TRXUSDT": "TRXUSDT",
    "XRPUSDT": "XRPUSDT",
    "BNBBTC": "BNBBTC",
    "ETHBTC": "ETHBTC",
    "LTCBTC": "LTCBTC",
    "TRXBTC": "TRXBTC",
    "XRPBTC": "XRPBTC",
    "LTCBNB": "LTCBNB",
    "TRXBNB": "TRXBNB",
    "XRPBNB": "XRPBNB",
}
