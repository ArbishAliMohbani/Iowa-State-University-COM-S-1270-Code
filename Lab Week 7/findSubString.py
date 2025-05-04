def findSubStringV1(str1, str2):
    v1 = str1.find(str2)
    return v1

def findSubStringV2(str1, str2):
    if str2 in str1:
        v2 = str1.index(str2)
        return v2
    else: 
        return -1

def findSubStringV3(str1, str2):
    for i in range(0, len(str1)):
        if(str1[i] == str2[0]):
            return i
    return -1        
    

def main():
    str1 = input("Enter a String: ")
    str2 = input("Enter a sub-string: ")
    v1 = findSubStringV1(str1, str2)
    print(v1)
    v2 = findSubStringV2(str1, str2)
    print(v2)
    v3 = findSubStringV3(str1, str2)
    print(v3)

if __name__ == "__main__":
    main()
