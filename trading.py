
import user_data as UD
import market_data as ms
import buyandsell
import math
import json
import threading

start = True
coin = ""
Amount = 1
open_trade = False

config = open("config.txt", "r")
content = config.readlines()
if content[0] == "COIN=SOL":
    coin = "SOL"
    print("SOL")

if content[0] == "COIN=BTC":
    coin = "BTC"
    print("BTC")

if content[0] == "COIN=ETH":
    coin = "ETH"
    print("ETH")

def USD_amount(balence):
    USD = balence / 10
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

def interface(api_key, api_secret):
    print(" ")
    print("All bot activity will be displayed here")
    print(" ")
    print("Type help for commands.")
    print(" ")

    while start == True:
        cmd = input("> ")

        if cmd == "help":
            print("bal --> returns your balence")
            print("orders --> returns all open orders")
            print("coin --> returns what coin is being traded")
            print("profit --> shows profit/loss from when the bot started until now")
            print("stop --> exits the program")

        if cmd == "bal":
            print("Your current main balence is: " + UD.user_balence(str(st.api_key), str(st.api_secret)))

        if cmd == "coin":
            print("The currently traded coin is: " + str(coin))



def bullish(open1, close2):
    if float(open1) < float(close2):
        return "Bull"
    
    if float(open1) > float(close2):
        return "Bear"
    
    else:
        return "Nothing"


def main(apiKey, apiSecret):
    api_key = apiKey
    api_secret = apiSecret
    Interface = threading.Thread(target=interface, args=(api_key, api_secret))
    while start == True:
        
        Amount = Trade_amount(float(USD_amount(UD.user_balence(api_key, api_secret))), str(coin))
        
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


        


