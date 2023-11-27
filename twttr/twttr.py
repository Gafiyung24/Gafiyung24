def main():
    n_v = shorten()
    print("Output: ", n_v)

#create function remove vowels
def shorten():
    n = input("Input: ")
#dictionary to contain vowels and an empty string
    v = {"a":"", "A":"", "E":"",  "e":"", "I":"", "i":"", "O":"", "o":"", "u":"", "U":""}
#for loop to iterate through the string
    for old, new in v.items():
        n = n.replace(old, new)
    return n
if __name__ == "__main__":
    main()
