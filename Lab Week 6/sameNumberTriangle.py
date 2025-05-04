def sameNumberTriangle(num):
    for j in range (1, num+1):
        for i in range(0, j):
            print(j, end=" ")
        print()

def main():
    num = int(input("Enter an Integer: "))
    sameNumberTriangle(num)

if __name__ == "__main__":
    main()