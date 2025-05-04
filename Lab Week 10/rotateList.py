def rotateList(num_list, rot):
    if(rot>0):
        new_list = []
        for i in range (len(num_list)-rot, len(num_list)):
            new_list.append(num_list[i])
        for j in range (0, len(num_list)-rot):
            new_list.append(num_list[j])
        return new_list
    elif(rot<0):
        new_list = []
        rot = (-1)*rot
        for j in range (rot, len(num_list)):
            new_list.append(num_list[j])
        for i in range (0, rot):
            new_list.append(num_list[i])
        return new_list

def gettingList():
    i = 1
    str_list = []
    while (i!=0):
        num = input("Enter an Integer: ")
        if(num!="*"):
            str_list.append(num)
        else: 
            i = 0 
    return str_list

def main():
    str_list = gettingList()
    num_list = []
    for i in range(0, len(str_list)):
        num_list.append(int(str_list[i]))
    rot = int(input("Enter an Integer Value: "))
    new_list = rotateList(num_list, rot)
    print(new_list)

if __name__ == "__main__":
    main()