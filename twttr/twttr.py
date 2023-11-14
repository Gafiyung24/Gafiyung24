def main():
    remove_vowels()
    print("Output: ", n)

#create function remove vowels
def remove_vowels():
    n = input("Input: ")
#dictionary to contain vowels and an empty string
    v = {"a":"", "e":"", "i":"", "o":"", "u":"" }
#for loop to iterate through the string
    for old, new in v.items():
        n = n.replace(old, new)
    return n
main()
