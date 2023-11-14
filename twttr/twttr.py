def main():
    remove_vowels()

#create function remove vowels
def remove_vowels():
    n = input("Input: ").split()
#dictionary to contain vowels and an empty string
    v = {"a":"", "e":"", "i":"", "o":"", "u":"" }
#for loop to iterate through the string
    for old, new in v.items():
        n = n.replace(old, new)
        n = 
main()
