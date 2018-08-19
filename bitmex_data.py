#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pusherclient
import pprint
import sys
import time, json, requests
import gdax
from websocket import WebSocketApp
from json import dumps, loads
from pprint import pprint

GDAX_URL = "wss://ws-feed.gdax.com"
BITSTAMP_APPKEY = "de504dc5763aeef9ff52"

VOLUME = 1

def  bitstamp_callback(*args, **kwargs):
    print("BITSTAM")
    return
    global bitstamp_price
    global bitstamp_sell
    global bitstamp_buy
    print("processing Args:", args)
    print("processing Kwargs:", kwargs)

def bitstamp_setup():

    def connect_handler(data):
        channel = pusher.subscribe('live_trades')
        channel.bind('trade', bitstamp_callback)

    appkey = BITSTAMP_APPKEY
    pusher = pusherclient.Pusher(appkey)
    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

class myWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com"
        self.products = ["ETH-USD"]
        self.message_count = 0
        print("Lets count the messages!")
    def on_message(self, msg):
        print("GDAX")
        return

        self.message_count += 1
        # pprint(msg)
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        print("-- Goodbye! --")

def main():
    bitstamp_setup()
    wsClient = myWebsocketClient()
    wsClient.start()
    while True:
    #     # Do other things in the meantime here...
        time.sleep(1)
        print("ITER")


if __name__ == '__main__':
    main()