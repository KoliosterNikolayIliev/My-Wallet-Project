from testnet_setup import DEBUG, SPOT_CLIENT

# give function calls as arguments to more_info(msg) to obtain information on which API is used (Test/Real)
# DBUG in testnet_setup must be true
LOGGING_BOOL = DEBUG


def return_account_info(client=SPOT_CLIENT):
    try:
        return client.account()
    except AttributeError as e:
        if LOGGING_BOOL:
            print(e)
        return 'KEY/SECRET not valid or not existing'


# return_account_info()


def get_my_trades(symbol="BTCBUSD", client=SPOT_CLIENT):
    """
        Account Trade List (USER_DATA)

        Get trades for a specific account and symbol.

        GET /api/v3/myTrades

        https://binance-docs.github.io/apidocs/spot/en/#account-trade-list-user_data

        Args:
            symbol (str)
        Keyword Args:
            fromId (int, optional): TradeId to fetch from. Default gets most recent trades.
            orderId (int, optional): This can only be used in combination with symbol
            startTime (int, optional)
            endTime (int, optional)
            limit (int, optional): Default Value: 500; Max Value: 1000
            recvWindow (int, optional): The value cannot be greater than 60000
        """
    try:
        return client.my_trades(symbol)
    except AttributeError as e:
        if LOGGING_BOOL:
            print(e)
        return 'KEY/SECRET not valid or not existing'

# get_my_trades()
