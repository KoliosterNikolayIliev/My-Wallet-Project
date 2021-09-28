"""
KEYS are for testnet ONLY !!! All users registering on the Spot Test Network
automatically receive a balance in many different assets.

How to generate keys:
    1. Register RSA key -> https://testnet.binance.vision/key/register
    https://testnet.binance.vision/ -> How can I use RSA Keys?

    2. Generate HMAC_SHA256 Key -> https://testnet.binance.vision/key/generate

    3. Save the Generated keys (if you loose the you need to revoke them and create new ones)
        -the needed keys are API key and Secret key generated in step 2.

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

# when key, secret are stored in environment variables.
# KEY = os.environ.get('binance_api')
# SECRET = os.environ.get('binance_secret')
test_key = "hGLWWbEWRKMLIP5gvo8dbwRWfQmgJRZZT9QBbWCfwGDO0chT3R1W3znALa18kT3B"
secret_key = "qgve977nb7LuuTUobjkcCUy2WWAcCodgW7GZI8PBYRJRwk33ZbrmRVLouEKkmyEN"

dimos_key = "bWjaqamFBtw8Rzi0xQ7ixgyvmIpakO9nwrBsfOZ6cbWLUdYFjHbhnhG9sy0k31SN"
dimos_secret_key = "J0uEwb9fKh1WTGW9P5CWd3XhJ771bWClznOQCv4YVsrvkijXRw0WARLwE6FdIypu"

KEY = test_key
SECRET = secret_key

real_base_url = 'https://api.binance.com'
test_base_url = 'https://testnet.binance.vision'
# for real API base_url=https://api.binance.com/api
SPOT_CLIENT = Client(key=KEY, secret=SECRET, base_url=test_base_url)

# make DEBUG False if functions need to return JSon data otherwise data will be printed in the console.

DEBUG = False
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


'''
tried pasting directly before row 97 in api.py from binance-connector library as a dirty patch and still the result is the same
print((requests.get(response.url, headers={'Content-Type':'application/json', 'X-MBX-APIKEY':'hGLWWbEWRKMLIP5gvo8dbwRWfQmgJRZZT9QBbWCfwGDO0chT3R1W3znALa18kT3B'})).json())
'''
