def multiplicationTable(lowNum, highNum):
    for j in range (lowNum, highNum+1):
        for i in range (lowNum, highNum+1):
            print(str(j*i), end="  ")
        print()
    
def main():
    lowNum = int(input("Tell me the lowest Number you want: "))
    highNum = int(input("Tell me the highest Number you want: "))
    multiplicationTable(lowNum, highNum)

if __name__ == "__main__":
    main()
