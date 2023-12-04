import os, sys
from PIL import Image, ImageOps
def main():
    check()
    paste()

def check():
    ext = (".jpg", "jpeg", "png")
    f1, ext1 = os.path.splitext(sys.argv[1])
    f2, ext2 = os.path.splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ext1.lower() not in ext and ext2.lower() not in ext:
        sys.exit("unknown extensions")
    elif ext1 != ext2:
        sys.exit("Input and Output have different extensions")

def paste():
    im_shirt = Image.open("shirt.png")
    size = im_shirt.size
    try:
        with Image.open(sys.argv[1]) as im1:
            ImageOps.fit(im1, size).save(sys.argv[2])
    except OSError:
        sys.exit("File can't be opened")
    else:
        with Image.open(sys.argv[2]) as im2:
            im2.paste(im_shirt, im_shirt)


if __name__ == "__main__":
    main()
