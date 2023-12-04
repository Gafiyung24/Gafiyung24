import os, sys
from PIL import Image
def main():

def check():
    ext = (".j)
    f1, ext1 = os.path.splitext(sys.argv[1])
    f2, ext2 = os.path.splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ext1 not in


if __name__ == "__main__":
    main()
