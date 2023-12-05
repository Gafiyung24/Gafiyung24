import os, sys
from PIL import Image, ImageOps
def main():
    shirt = "shirt.png"
    check()
    paste(shirt, sys.argv[1], sys.argv[2])


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

def paste(n0, n1, n2):
    im_shirt = Image.open(n0)
    size = im_shirt.size
    #mask = im_shirt.convert("L")
    #mask = im_shirt.split()[3]
    try:
        with Image.open(n1) as im1:
            ImageOps.fit(im1, size)
            im1.paste(im_shirt, im_shirt)
            return im1.save(n2)
    except OSError:
        sys.exit("File can't be opened")
    """else:
        with Image.open(n1) as im2:
            im2.paste(im_shirt, im_shirt)
            return im2.save(n2)"""
    
if __name__ == "__main__":
    main()
