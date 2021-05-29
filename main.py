import ccxt
import json
import numpy as np
import time

exchanges = ccxt.exchanges
symbols = ["ADA/BTC", "BCH/BTC", "BTG/BTC", "BTS/BTC", "CLAIM/BTC", "DASH/BTC", "DOGE/BTC", "EDO/BTC", "EOS/BTC",
           "ETC/BTC","ETH/BTC", "FCT/BTC", "ICX/BTC", "IOTA/BTC", "LSK/BTC", "LTC/BTC", "MAID/BTC", "NEO/BTC",
           "OMG/BTC", "QTUM/BTC", "STR/BTC", "TRX/BTC","VEN/BTC", "XEM/BTC", "XLM/BTC", "XMR/BTC", "XRP/BTC", "ZEC/BTC"]
clients = [getattr(ccxt, e.lower())() for e in exchanges]

ask = np.zeros((len(symbols), len(clients)))
bid = np.zeros((len(symbols), len(clients)))

symlen = len(symbols)
clilen = len(clients)

bef = time.time()
print(bef)
#in a more efficient scenario, we would look for profitable opportunities within the loop
symbol = 0
for rowidx, symbol in enumerate(symbols):
    for idx, client in enumerate(clients):
        try:
            book = client.fetch_order_book(symbol)
            ask[rowidx, idx] = book['asks'][0][0]
            bid[rowidx, idx] = book['bids'][0][0]
        except:
            pass

aft = time.time()
total = aft - bef

print(total)


fee = 0.25

opportunities = []
 
for i, symbol in enumerate(symbols):
    for j1, exchange1 in enumerate(exchanges):
        for j2, exchange2 in enumerate(exchanges):
            
            roi = 0
            if j1 != j2 and ask[i, j1]>0:
                roi = ((bid[i, j2]*(1-fee/100)) / (ask[i, j1]*(1+fee/100)) - 1) * 100
                
                if roi>0:
                    opportunities.append([symbol, exchange1, ask[i, j1], exchange2, bid[i, j2], round(roi,2)])
                
print("Number of profitable opportunities:", len(opportunities))
print(opportunities)