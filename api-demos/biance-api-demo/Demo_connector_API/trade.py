import logging

from binance.error import ClientError

from Demo_connector_API.decorators import require_auth
from testnet_setup import DEBUG, SPOT_CLIENT

# give function calls as arguments to more_info(msg) to obtain information on which API is used (Test/Real)
# DBUG in testnet_setup must be true
LOGGING_BOOL = DEBUG


@require_auth
def return_account_info(client=SPOT_CLIENT):
    return client.account()


# return_account_info()

@require_auth
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

    return client.my_trades(symbol)


# get_my_trades()

@require_auth
def get_account_orders(symbol="BTCBUSD", client=SPOT_CLIENT):
    try:
        if DEBUG:
            return logging.info(client.get_orders(symbol))
        result = client.get_orders(symbol)
        return result

    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )



