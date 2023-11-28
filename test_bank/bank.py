def main():
    x = input("Greeting: ")
    print(f"${value(x)})

def value(greeting):
    greetings = greeting.lower().strip()
    if "hello" in greetings:
        value = 0
    elif greetings.find("h") == 0 and "hello" not in greetings :
        value = 20
    else:
        value = 100
    return value
if __name__ == "__main__":
    main()

