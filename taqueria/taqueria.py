def main():
    menu_t = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total_price = total(get_order(menu_t))
    print(f"Total: ${total_price}")



def get_order(menu): #function to get user input and handle errors
    items = []
    while True:
        try:
            items.append(menu.get(input("Items: ").capitalize()))

        except KeyError:
            pass

        except EOFError:
            return items

def total(items): #function to get total of items picked
    t = sum(items)
    return t




main()

