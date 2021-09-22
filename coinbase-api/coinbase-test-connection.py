"""
Testing the connection with Coinbase.com
Try to get BTC-USD data for 20 seconds.
Count number of successful messages from the server.
"""

import cbpro
import time

api_secret = 'c3rW1IVh/Xp7P8K8IOS9kpW2veTgleBQ+yRV6DA84ZlUfpa8l1nYoDY3POUlE1/kfoDGFSKkbzAF14HSSufoJA=='
api_key = 'd862aea8a0e5cdcbe01ed3835916f9eb'
api_pass = '860805'


""" 
Inherit from WebsocketClient class 
and overwrite 3 methods
"""

class TextWebSocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = 'wss://ws-feed-public.sandbox.pro.coinbase.com'
        self.message_count = 0

    def on_message(self, msg):
        self.message_count += 1
        msg_type = msg.get('type', None)
        if msg_type == 'ticker':
            time_stamp = msg.get('time', ('-'*27))
            price = msg.get('price', None)
            price = float(price) if price is not None else 'None'
            product_id = msg.get('product_id', None)

            print(f"{product_id} / {price:.3f} USD /  channel type:{msg_type} / datestamp: {time_stamp:30} ")

    def on_close(self):
        print(f"Connection was successfully closed by the script. Total received messages: {self.message_count}")


test = TextWebSocketClient(products=['BTC-USD'], channels=['ticker'])

test.start()
time.sleep(20)
test.close()
