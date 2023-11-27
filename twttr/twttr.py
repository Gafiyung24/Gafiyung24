def main():

    n = input("Input: ")
    n_v = shorten(n)
    print("Output: ", n_v)

#create function remove vowels
def shorten(word):

#dictionary to contain vowels and an empty string
    v = {"a":"", "A":"", "E":"",  "e":"", "I":"", "i":"", "O":"", "o":"", "u":"", "U":""}
#for loop to iterate through the string
    for old, new in v.items():
        word = word.replace(old, new)
    return word
if __name__ == "__main__":
    main()
