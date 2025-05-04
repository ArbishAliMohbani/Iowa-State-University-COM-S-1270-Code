def endNum(num_list, num):
    j = -1
    temp = 0
    for i in range(0, len(num_list)):
        if (num == num_list[i]):
                num_list.remove(num_list[i])
                num_list.append(num)            

    return num_list


def generateList():
    i = 1
    str_list= []
    while(i!=0):
        num = input("Enter an Integer: ")
        if(num!="*"):
            str_list.append(num)
        else:
            i=0
    return str_list

def main():
    str_list = generateList()
    num_list = []
    for i in range(0, len(str_list)):
        num_list.append(int(str_list[i]))
    num = int(input("Enter an Integer you have already put in: "))
    new_list = endNum(num_list, num)
    print(new_list)

if __name__ == "__main__":
    main()
