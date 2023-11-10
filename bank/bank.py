x = input("Greeting: ").lower().strip()
if "hello" in x is True:
    print("$0")
elif x.find("h") == 0 and x != "helllo":
    print("$20")
else:
    print("$100")

