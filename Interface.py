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
