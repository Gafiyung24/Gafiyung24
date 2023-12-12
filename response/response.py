from validator_collection import validators, checkers, errors

def main():
    print(checker(input("What's your email address? ")))


def checker(s):
    response = checkers.is_email(s)
    if response:
        return "valid"
    else:
        return "invalid"




if __name__ == "__main__":
    main
