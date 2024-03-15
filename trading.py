
import user_data as UD
import market_data as ms
import buyandsell
import math
import json
import threading
import interface

start = False
coin = "SOL_USD"
Amount = 1
open_long = False

def USD_amount(balence):
    USD = float(balence) / 10
    return USD

def Trade_amount(usd, instrument):
    coin_price = ms.coin_price(str(instrument))
    coin_div_usd = float(coin_price) / float(usd)
    amount = 1 / float(coin_div_usd)
    return amount

def RedGreen(open, close):
    if float(open) > float(close):
        return "Red"
    if float(close) > float(open):
        return "Green"

def open_trade(open_orders):
    if open_orders.open == True:
        open_trade = True

def bullish(open1, close2):
    if float(open1) < float(close2):
        return "Bull"
    if float(open1) > float(close2):
        return "Bear"
    else:
        return "Nothing"

def main(apiKey, apiSecret):
    start = True
    api_key = apiKey
    api_secret = apiSecret
    interface.interface(str(api_key), str(api_secret))
    while start == True:
        
        Amount = Trade_amount(float(USD_amount(UD.user_balence(api_key, api_secret))), "SOL_USD")
        
        newest_candle = ms.last_candles(0, str(coin))
        latest_10_candles = ms.last_candles(10, str(coin))

        #Algo
        if bullish(newest_candle["o"], latest_10_candles[1]["c"]) == "Bull":
            print("Bull")

        elif bullish(newest_candle["o"], latest_10_candles[1]["c"]) == "Bear":
            print("Bear")

        elif bullish(newest_candle["o"], latest_10_candles[1]["c"]) == "Nothing":
            print("Nothing")
        
        time.sleep(5)


        


