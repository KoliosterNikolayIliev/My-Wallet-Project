import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

from testnet_setup import KEY, SECRET, DEBUG

# for real API base_url=https://api.binance.com/api
SPOT_CLIENT = Client(key=KEY, secret=SECRET, base_url="https://testnet.binance.vision")

LOGGING_BOOL = DEBUG

if LOGGING_BOOL:
    config_logging(logging, logging.DEBUG)

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


def get_aggregate_traders(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    """Get compressed, aggregate trades. Trades that fill at the time,
    from the same order, with the same price will have the quantity aggregated."""

    # fromId -> id to get aggregate trades from INCLUSIVE.
    # BTCUSDT -> type of coins
    # spot_client.agg_trades(symbol, limit=10, fromId="")

    return spot_client.agg_trades(symbol)


# Example function call - use SYMBOLS dict for reference
# get_aggregate_traders("BTCUSDT")

def get_average_price(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    return spot_client.avg_price(symbol)


# Example function call - use SYMBOLS dict for reference
# logging.info(get_average_price("BTCUSDT"))

def book_ticker(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    return spot_client.book_ticker(symbol)


# book_ticker()

def depth(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    """
    spot_client.depth("BTCUSDT", limit=10) - limit (int, optional):
    limit the results. Default 100; valid limits:[5, 10, 20, 50, 100, 500, 1000, 5000]
    """
    return spot_client.depth(symbol)


# depth()

def get_exchange_info(symbol="BTCBUSD", symbols=["BTCUSDT", "BNBUSDT"], spot_client=SPOT_CLIENT):
    """Exchange Information
        Current exchange trading rules and symbol information

        GET /api/v3/exchangeinfo

        https://binance-docs.github.io/apidocs/spot/en/#exchange-information

         Args:
            symbol (str, optional): the trading pair
            symbols (list, optional): list of trading pairs
        """
    # logging.info(spot_client.exchange_info())
    # logging.info(spot_client.exchange_info(symbol=symbol))
    return spot_client.exchange_info(symbols=symbols)


# get_exchange_info()


def get_historical_trades(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    """Old Trade Lookup
       Get older market trades.

       GET /api/v3/historicalTrades

       https://binance-docs.github.io/apidocs/spot/en/#old-trade-lookup

       Args:
           symbol (str): the trading pair
       Keyword Args:
           limit (int, optional): limit the results. Default 500; max 1000.
           formId (int, optional): trade id to fetch from. Default gets most recent trades.
       """
    # historical_trades requires api key in request header

    return spot_client.historical_trades(symbol)


# get_historical_trades()


def get_klines(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    """Kline/Candlestick Data

        GET /api/v3/klines

        https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

        Args:
            symbol (str): the trading pair
            interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
        Keyword Args:
            limit (int, optional): limit the results. Default 500; max 1000.
            startTime (int, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
            endTime (int, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
        """
    return spot_client.klines(symbol, "1m")


# get_klines()


def ticker_24hr(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    """
        24hr Ticker Price Change Statistics

         GET /api/v3/ticker/24hr

         https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

         Args:
             symbol (str, optional): the trading pair
     """
    spot_client.ticker_24hr(symbol)


# ticker_24hr()

def get_ticker_price(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    """
        Symbol Price Ticker

        GET /api/v3/ticker/price

        https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker

        Args:
            symbol (str, optional): the trading pair
    """
    return spot_client.ticker_price(symbol)


# get_ticker_price()

def get_trades(symbol="BTCBUSD", spot_client=SPOT_CLIENT):
    """
        Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        Args:
            symbol (str): the trading pair
        Keyword Args:
            limit (int, optional): limit the results. Default 500; max 1000.
    """
    return spot_client.trades("BTCUSDT")

# get_trades()