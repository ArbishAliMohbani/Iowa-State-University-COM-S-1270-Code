# Arbish Ali Mohbani                02/22/2025
# Matthew Holman
# Lab # 5

def findLeapYear(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print(str(year)+" is a Leap Year!")
            else:
                print(str(year)+" is not a Leap Year!")
        else:
            print(str(year)+" is a Leap Year!")
    else:
        print(str(year)+" is not a Leap Year!")

def main():
    year = int(input("Enter a Year: "))
    findLeapYear(year)


if __name__ == "__main__":
    main()
