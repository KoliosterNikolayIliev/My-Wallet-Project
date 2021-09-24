from pprint import pprint

import testnet_setup
from Demo_connector_API.market import get_average_price, get_book_ticker, get_depth, get_exchange_info, \
    get_historical_trades, get_klines, get_ticker_24hr, get_ticker_price, get_trades

from Demo_connector_API.trade import return_account_info, get_my_trades

FUNCTIONS_LIST = {
    1: get_average_price,
    2: get_book_ticker,
    3: get_depth,
    4: get_exchange_info,
    5: get_historical_trades,
    6: get_klines,
    7: get_ticker_24hr,
    8: get_ticker_price,
    9: get_trades,
    10: return_account_info,
    11: get_my_trades,
}


def start():
    print("If you want to enable logging go to testnet_setup.py and set DEBUG to True")
    print("To exit the console type 'exit' instead of option\n")
    for key, value in FUNCTIONS_LIST.items():
        print(f"{key}: {value.__name__}")

    while True:
        print("Please choose an option (integer from the list of options) or type exit to exit:")
        a = input()
        if a == "exit":
            break
        if testnet_setup.DEBUG:
            FUNCTIONS_LIST[int(a)]()
        else:
            pprint(FUNCTIONS_LIST[int(a)]())


if __name__ == '__main__':
    start()
