import os, sys
from PIL import Image
def main():

def check():
    ext = (".jpg", "jpeg", "png")
    f1, ext1 = os.path.splitext(sys.argv[1])
    f2, ext2 = os.path.splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ext1.lower() not in ext and ext2.lower() not in ext:
        sys.exit("Input and Output have different extensions")
    elif ext1 != ext2:
        sys.exit("Unknown file type")


if __name__ == "__main__":
    main()
