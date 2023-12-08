import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if match:
        for i in range(4):
            if int(match.group(i+1)) > 255:
                return False
            else:
                return True

    else:
        return False


if __name__ == "__main__":
    main()
