def main():
    x = input("Greeting: ").lower().strip()
    print(value(x))

def value(greeting):
    if "hello" in greeting:
        value = "$0"
    elif greeting.find("h") == 0 and "hello" not in greeting :
        value = "$20"
    else:
        value = "$100"
    return value

