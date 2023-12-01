import sys
def main():
    f = check_arg()
    c = read(f)
    print(c)


def check_arg():
    #check for condtions of command line argumemts
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command_line arguments")
    elif sys.argv[1].find(".py") == -1:
        sys.exit("File doesn't exist")
    return sys.argv[1]

def read(n):
    count = 0
    try:
        with open(n, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File doesn't exist")
    else:
        for line in lines:
            if line.strip().startswith("#") == False:
                count += 1
    return count

if __name__ == "__main__":
    main()
