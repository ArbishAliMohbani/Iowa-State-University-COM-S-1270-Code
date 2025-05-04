def reverseStringV1(str1):
    v1 = str1[::-1]
    return v1

def reverseStringV2(str1):
    v2 = ("".join(reversed(str1)))
    return v2

def reverseStringV3(str1):
    v3 = ""
    for i in range(len(str1)-1, -1, -1):
        v3+=str1[i]
    return v3

def reverseStringV4(str1):
    v4 = ""

def reverseStringV5(str1):
    v5 = ""
    i = len(str1)-1
    while(i!=-1):
        v5+=str1[i]
        i-=1
    return v5

def main():
    str1 = input("Enter a string: ")
    v1 = reverseStringV1(str1)
    print("Version 1: "+v1)
    v2 = reverseStringV2(str1)
    print("Version 2: "+v2)
    v3 = reverseStringV3(str1)
    print("Version 3: "+v3)
    v5 = reverseStringV5(str1)
    print("Version 5: "+v5)

if __name__ == "__main__":
    main()