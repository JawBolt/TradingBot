
import user_data as UD
import trading
import time

print(" ")
print("Crypto Trading bot V2")
print("By JawBolt (George)")
print(" ")

api_key = input("Enter your API Key: " )
api_secret = input("Enter your Secret Key: ")

if float(UD.user_balence(str(api_key), str(api_secret))) > 0:
    print(" ")
    print("Succesful login!")
    print(" ")
    print("Your current Balence is $", str(UD.user_balence(str(api_key), str(api_secret))))
    print(" ")
    print("Starting...")
    trading.main(str(api_key), str(api_secret))

else:
    print(" ")
    print("Invalid keys or unable to connect!")
    print("Exiting...")
    time.sleep(2)
    exit()
