
import user_data as UD
import market_data as ms
import buyandsell
import math
import json

coin = ""
config = open("config.txt", "r")
content = config.readlines()
if content[0] == "COIN=SOL":
    coin = "SOL"
running = True



def main(api_key, api_secret):
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
            print("The currently traded coin is: " + )

