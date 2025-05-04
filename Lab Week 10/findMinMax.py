def gettingList():
    i = 1
    str_List = []
    while(i!=0):
        num = input("Enter an integer: ")
        if(num!="*"):
            str_List.append(num)
        else:
            i = 0
    return str_List

def findMin(num_list):
    min = num_list[0]
    for i in range(1, len(num_list)):
        if(min>num_list[i]):
            min = num_list[i]
    return min
        
def findMax(num_list):
    max = num_list[0]
    for i in range(1, len(num_list)):
        if(max<num_list[i]):
            max = num_list[i]
    return max

def main():
    str_List = gettingList()
    num_list = []
    for i in range(0, len(str_List)):
        num_list.append(int(str_List[i]))
    min = findMin(num_list)
    max = findMax(num_list)
    print("The Minimum value is: "+str(min)+"\nThe Maximum value is: "+str(max))


if __name__ == "__main__":
    main()