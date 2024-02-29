
import user_data as UD
import market_data as ms
import buyandsell
import math
import json
import threading

coin = ""

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


running = True

def USD_amount(usd, instrument):
    coin_price = ms.coin_price(str(instrument))
    coin_div_usd = float(coin_price) / float(usd)
    amount = 1 / float(coin_div_usd)
    return amount

def main(api_key, api_secret):
    while running == True:
        


def interface(api_key, api_secret):
    print(" ")
    print("All bot activity will be displayed here")
    print(" ")
    print("Type help for commands.")
    print(" ")

    while running == True:
        cmd = input("> ")

        if cmd == "help":
            print("bal --> returns your balence")
            print("orders --> returns all open orders")
            print("stop --> stops the bot temporarily")
            print("coin --> returns what coin is being traded")
            print("profit --> shows profit/loss from when the bot started until now")
            print("shutdown --> exits the program")

        if cmd == "bal":
            print("Your current main balence is: " + UD.user_balence(str(api_key), str(api_secret)))

        if cmd == "coin":
            print("The currently traded coin is: " + str(coin))

        

        
        


        


