def starRightTriangle(num):
    for j in range(0, num+1):
        for i in range(0, j):
            print("*", end=" ")

        print()

def main():
    num = int(input("Enter an Integer: "))
    starRightTriangle(num)

if __name__ == "__main__":
    main()