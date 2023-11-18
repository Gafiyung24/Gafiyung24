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







def get_order(menu): #function to get user input and handle errors
    items = []
    while True:
        try:
            items.append(get(input("Item: ").capitalize()[menu]))
        except(EOFError, KeyError):
            pass



main()

