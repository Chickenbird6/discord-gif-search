dataFile = "gifs.txt"

menu = "1. Find gifs by keyword(s)\n" \
       "2. List all gifs\n" \
       "3. Save a gif\n"

def printAll():
    f = open(dataFile, "rt")
    print(f.read(), end="")
    f.close()

def getLinesContaining():
    print("Enter keyword: ", end="")
    keyword = input()
    print("--------------------")
    f = open(dataFile, "rt")
    # loop through all lines in the file
    for i in f:
        # check the line for the string
        if keyword in i:
            # return the line
            print(str(i), end="")
        # safely close the file
    f.close()

def saveGif():
    name = ""
    link = ""
    print("Enter the name or keywords for the gif: ", end="")
    name = input()
    print("--------------------")
    print("Enter the link to the gif: ", end="")
    link = input()
    print("--------------------")
    f = open(dataFile, "at")
    f.write(name + " | " + link + "\n")
    f.close()

while True:
    print(menu, end="")
    print("--------------------")
    print("Enter action: ", end="")
    choice = input()
    print("--------------------")

    if choice == "1":
        getLinesContaining()
        print("--------------------")
    elif choice == "2":
        printAll()
        print("--------------------")
    elif choice == "3":
        saveGif()
