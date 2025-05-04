import random

def wordSwap(str1):
    str_list1 = str1.split(" ")
    str_list2 = str_list1.copy()
    length = len(str_list1)
    count = 0
    fin_list= []
    str_dict = {}
    for i in range(0, length):
        for j in range(0, length):
            if (str_list1[i] == str_list1[j]):
                count += 1
        if(count>1):
            str_list1[i] = "!"
        count = 0    
    for y in range(0, len(str_list1)):
        if(str_list1[y].isalpha()):
            fin_list.append(str_list1[y])

    for x in range(0, len(fin_list)):
        str_dict[fin_list[x]] = ""

    keys = str_dict.keys()
    for keys in str_dict:
        str_dict[keys] = str_list2[random.randrange(0, len(str_list2)-1)]
    print(str_dict.items())

def main():
    str1 = input("Enter a string: ")
    wordSwap(str1)

if __name__ == "__main__":
    main()