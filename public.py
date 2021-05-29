import requests
from datetime import datetime
import time
import json
from krakenkey import *

# BINANCE
binance_api_url = "https://api.binance.us/"
base_endpoint = "api/v3/"

binance_ticker = "ETHBTC"
binance_query = {"symbol": binance_ticker}
binance_data = requests.get(binance_api_url + base_endpoint + "ticker/bookTicker", params=binance_query)

def b_getcurrentbidask():
    book = binance_data.json()
    b_timestamp = int(requests.get(binance_api_url + base_endpoint + "time").json()['serverTime'])
    b_time = datetime.fromtimestamp(b_timestamp/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    bidask = ["Binance", binance_ticker, b_timestamp, b_time, book['bidPrice'], book['askPrice']]

    return bidask

# KRAKEN
kraken_API_PUBLIC_KEY = public_kraken
kraken_api_url = "https://api.kraken.com/"
public = "0/public/"

kraken_ticker = "XETHXXBT"
kraken_query = {'pair':kraken_ticker}
kraken_data = requests.get(kraken_api_url + public + "Spread", params=kraken_query)

def k_getcurrentbidask(kticksymbol):
    spread = kraken_data.json()['result'][kticksymbol][-1]
    spread.insert(1, datetime.fromtimestamp(spread[0]).strftime('%Y-%m-%d %H:%M:%S'))
    spread.insert(0, "Kraken")
    spread.insert(1, kticksymbol)
    return spread

# pairs = {}

# for pair in kraken_data.json()['result']:
#     try:
#         pairs[pair] = kraken_data.json()['result'][pair]['wsname']
#     except:
#         pass

print(json.dumps(k_getcurrentbidask(kraken_ticker), indent=2))

print(json.dumps(b_getcurrentbidask(), indent=2))
