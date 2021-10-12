from pprint import pprint

import testnet_setup
from Demo_connector_API.create_orders_for_testing import make_order
from Demo_connector_API.live_data import get_live_account_data, get_live_combined_data, get_live_trade_data, test_live_data
from Demo_connector_API.market import get_average_price, get_book_ticker, get_depth, get_exchange_info, \
    get_historical_trades, get_klines, get_current_price_24h, get_current_price, get_trades

from Demo_connector_API.trade import get_account_info, get_my_trades, get_account_orders

FUNCTIONS_LIST = {
    123: 'exit_program',
    # 0: make_order,
    1: get_average_price,
    # 2: get_book_ticker,
    # 3: get_depth,
    4: get_exchange_info,
    5: get_historical_trades,
    # 6: get_klines,
    7: get_current_price_24h,
    8: get_current_price,
    9: get_trades,
    10: get_account_info,
    11: get_my_trades,
    12: get_account_orders,
    13: test_live_data,
    14: get_live_account_data,
    15: get_live_combined_data,
    16: get_live_trade_data,

}


def start():
    print("If you want to enable logging go to testnet_setup.py and set DEBUG to True")
    print("To exit the console type 'exit' instead of option digit\n")
    print("data is returned as python dictionaries. I can be dumped to JSON")
    for key, value in FUNCTIONS_LIST.items():
        print(f"{key}: {value}") if type(value) is str else print(f"{key}: {value.__name__}")

    while True:
        print("\nPlease choose an option (integer from the list of options) or type exit to exit:\n")
        a = input()
        try:
            if a == '123':
                break
            if testnet_setup.DEBUG:
                FUNCTIONS_LIST[int(a)]()
            else:
                pprint(FUNCTIONS_LIST[int(a)]())
        except KeyError as e:
            print('Unavailable option!!!')


if __name__ == '__main__':
    start()
