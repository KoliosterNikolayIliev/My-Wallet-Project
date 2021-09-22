"""
Testing the connection with Coinbase.com
Try to get BTC-USD data for 20 seconds.
Count number of successful messages from the server.
"""

import cbpro
import time
import access_data

api_secret = access_data.api_secret
api_key = access_data.api_key
api_pass = access_data.api_pass


""" 
Inherit from WebsocketClient class 
and overwrite 3 methods
"""

class TextWebSocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = 'wss://ws-feed-public.sandbox.pro.coinbase.com'
        self.message_count = 0

    def on_message(self, msg):
        msg_type = msg.get('type', None)
        if msg_type == 'ticker':
            time_stamp = msg.get('time', ('-'*27))
            price = msg.get('price', None)
            price = float(price) if price is not None else 'None'
            product_id = msg.get('product_id', None)

            print(f"{product_id} / {price:.3f} USD /  channel type:{msg_type} / datestamp: {time_stamp:30} ")
            self.message_count += 1

    def on_close(self):
        print(f"Connection was successfully closed by the script. Total received messages: {self.message_count}")


test = TextWebSocketClient(products=['BTC-USD'], channels=['ticker'])

test.start()
time.sleep(20)
test.close()
