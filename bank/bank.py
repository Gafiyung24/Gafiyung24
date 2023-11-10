x = input("Greeting: ").lower().strip()
if "hello" in x:
    print("$0")
elif x.find("h") == 0 and "hello" not in x :
    print("$20")
else:
    print("$100")

