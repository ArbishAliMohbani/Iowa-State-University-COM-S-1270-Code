#def removeNonASCII():

def readFile(file_name):
    f = open(file_name, "r")
    file_content = f.read()
    f.close()
    clean = ""
    for i in range(0, len(file_content)):
        if (ord(file_content[i]) == 32):
            clean+=file_content[i]
        elif (ord(file_content[i]) == 10):
            clean+=file_content[i]
        elif (ord(file_content[i])>=65 and ord(file_content[i])<=90):
            clean+=file_content[i]
        elif (ord(file_content[i])>=97 and ord(file_content[i])<=122):
             clean+=file_content[i]
    return clean

def main():
    file_name = input("Enter the file name you want: ")
    clean = readFile(file_name+".txt")
    f = open((file_name+"_clean.txt"), "w")
    f.write(clean)
    f.close()
    

if __name__ == "__main__":
    main()