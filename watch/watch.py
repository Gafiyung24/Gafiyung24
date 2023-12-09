import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"', s)
    if match:
        url_n = match.group(1)
        return f"https://youtu.be/{url_n}"
    else:
        return None





if __name__ == "__main__":
    main()
