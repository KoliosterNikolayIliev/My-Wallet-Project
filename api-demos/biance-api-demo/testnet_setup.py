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

KEY = os.environ.get('binance_api')
SECRET = os.environ.get('binance_secret')
# make logging False if functions need to return JSon data otherwise data will be printed in the console.
# give function calls as arguments(msg) to logging.info(msg) to obtain which API is used (Test/Real)
DEBUG = True