x = input("Greeting: ").lower().strip()
if "hello" in x:
    print("$0")
elif x.find("h") == 0 and "hello" in x is False:
    print("$20")
else:
    print("$100")

