import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"




if __name__ == "__main__":
    main()
