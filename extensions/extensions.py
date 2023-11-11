# initialising variable to receive user input and replace make jpg the same as jpeg
x = input("File name: ").strip().lower().replace("jpg", "jpeg")

#checking error incase . is not in entry
if x.find(".") == -1:
    print("application/octet-stream")
#for more than one extension
elif x.count(".") == 2:
     x = x.split(".")
     #x1 = x.split(".")[1].strip()
     print(x)
'''
#getting substring for file extension
else:
    x1 = x.split(".")[1].strip()

# condtional statement to find the type of file extensions
match x1:
    case "gif" | "jpeg" | "png":
        print(f"image/{x1}")
    case "pdf" | "zip":
        print(f"application/{x1}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
'''
