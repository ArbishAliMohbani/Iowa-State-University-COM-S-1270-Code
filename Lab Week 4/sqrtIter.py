def sqrtiter(x1, i1):
    temp = int(1)
    for j in range(1, i1+1):
        temp = ((x1/temp)+temp)/2

    return temp

def main():
    x = int(input("Enter the Number you want square root for: "))
    i = int(input("Enter how many iterations do you want: "))
    root = sqrtiter(x, i)
    print("The square root by approximation is: "+str(root))

if __name__ == "__main__":
    main()
