x = input("Greeting: ").lower().strip()
if x.find("hello") == True:
    print("$0")
elif x.find("h") == 0 and x.find("hello") == True:
    print("$20")
else:
    print("$100")

