x = input("Greeting: ").lower().strip()
if x == "hello" or x.find("hello") == 0:
    print("$0")
elif x.find("h") == 0 and x != "helllo":
    print("$20")
else:
    print("$100")

