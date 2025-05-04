def palindromeCheckV1(str1):
    v1 = ""
    for i in range(len(str1)-1, -1, -1):
        v1+=str1[i]
    if(str1 == v1):
        return ("Palindrome")
    else:
        return ("Not a Palindrome")

def palindromeCheckV2(str1):
    j=-1
    for i in range(0, len(str1)):
        if(str1[i] != str1[j]):
            return ("Not a Palindrome")
        j-=1
    return ("Palindrome")

def main():
    str1 = input("Enter a string: ")
    v1 = palindromeCheckV1(str1)
    print("'"+str1+"'"+" is: "+v1)
    v2 = palindromeCheckV2(str1)
    print("'"+str1+"'"+" is: "+v2)

if __name__ == "__main__":
    main()