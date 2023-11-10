x = input("Greeting: ").lower().strip()
if x == "hello":
    print("$0")
elif x.find("h") == 0 and x != "helllo":
    print("$20")
else:
    print("$100")

