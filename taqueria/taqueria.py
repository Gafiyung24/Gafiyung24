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
    get_order(menu_t)
    print('\n'f"Total: ${total_price:.2f}")


def get_order(menu): #function to get user input and handle errors
    items = [0]
    while True:
        try:
            items.append(menu.get(input("Items: ").title()))


        except KeyError:
            pass

        except EOFError:
            return total_price == total(items)

def total(items): #function to get total of items picked
    t = sum(items)
    return t

main()

