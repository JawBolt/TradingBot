
import user_data as UD
#import trading
import time

print(" ")
print("Crypto Trading bot V2")
print("By JawBolt (George)")
print(" ")

api_key = input("Enter your API Key: " )
api_secret = input("Enter your Secret Key: ")
try:
    UD.user_balence(str(api_key), str(api_secret))
    print(" ")
    print("Succesful login!")
    print(" ")
    print("Your current Balence is $", UD.user_balence(str(api_key), str(api_secret)))
    print(" ")
    print("Starting...")
    trading.start = True

except:
    print(" ")
    print("Invalid keys or unable to connect!")
    print("Exiting...")
    time.sleep(2)
    exit()
