def palindromeList(str_list):
    status = True
    j=0
    for i in range (len(str_list)-1, -1, -1):
        if(str_list[i]==str_list[j]):
            if(status != False):
                status = True
        else: 
            status = False
        j+=1
    return status
            

def gettingList():
    i = 1
    str_List = []
    while(i!=0):
        str1 = input("Enter a string: ")
        if(str1!="*"):
            str_List.append(str1)
        else:
            i = 0
    return str_List

def main():
    str_list = gettingList()
    pallist = palindromeList(str_list)
    print(pallist)

if __name__ == "__main__":
    main()