"""input("What is your name? :")
print("hello, World")
print("meow\n" * 3, end= "")
def main():
    print_column(3)



def print_column(height):
    for _ in range(height):
        print("#" * 3)

def main():
    g = input("fraction: ").split("/")
    print(f"{divide(g)}")


def divide(x):
    x_d = x[0] / x[1]
    return x_d
main()"""



"""menu_t = {
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
sentences = [
    'This is the first sentence.',
    'The second sentence is here.',
    'And this is the third sentence.'
]

# Initialize an empty dictionary to store counts
word_counts = {}

# Count word repetitions in the list
for sentence in sentences:
    words = sentence.split()
    for word in words:
        # Use the get() method to get the current count or default to 0
        current_count = word_counts.get(word, 0)

        # Increment the count
        word_counts[word] = current_count + 1

# Display the counts
for word, count in word_counts.items():
    print(f"{word}: {count} times")
"""
days = [range(31)]
print(days)



