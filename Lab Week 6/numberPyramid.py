def numberPyramid(num):
    temp = num
    for j in range (1, num+2):
        print(" "*temp, end="")
        for i in range (1, j):
            print(i, end=" ")
        temp-=1
        print()

def main():
    num = int(input("Enter an Integer: "))
    numberPyramid(num)

if __name__ == "__main__":
    main()