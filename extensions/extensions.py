# initialising variable to receive user input and create substring for file extension
x = input("File name: ").strip().lower()
x1 = x.split(".")[1].strip()

# condtional statement to find the type of file extensions
match x1:
    case "gif" | "jpg" | "jpeg" | "png":
        print(f"image/{x1}")
    case 

