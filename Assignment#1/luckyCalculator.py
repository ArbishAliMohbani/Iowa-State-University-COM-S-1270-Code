# Arbish Ali Mohbani             02/12/2025
# Assignment # 2
# Matthew Holman [COM S 1270]
# This Code can do 7 type of calculations and can also generate a lucky number!

import random

def luckyCalculator(a, b, operator):
    if ((operator == "/" and b == 0) or (operator == "//" and b == 0)):
        print("Error! 0 can't be used with '/' or '//'")
    else:
        if (operator == "+"):
            print("The sum of these 2 integers is: "+str(a+b))
        elif (operator == "-"):
            print("The difference of these 2 integers is: "+str(a-b))
        elif (operator == "*"):
            print("The product of these 2 integers is: "+str(a*b))
        elif (operator == "/"):
            print("The quotient of these 2 integers is: "+str(a/b))
        elif (operator == "//"):
            print("The quotient of these 2 integers is: "+str(a//b))
        elif (operator == "%"):
            print("The remainder of these 2 integers is: "+ str(a%b))
        elif (operator == "**"):
            print("The power of these 2 integers is: "+str(a**b))

def luckyNumber(c, d):
    print("Your Lucky Number is: "+str(random.randrange(c, d)))

def main():
    choose = input("What would you like to do?\n[c]alculator, [l]ucky number, [q]uit: ")
    if (choose == "c" or choose == "C"):
        selection = input("Please Choose a Calculation: [+], [-], [*], [/], [//], [%], [**]: ")
        if(selection == "+" or selection == "-" or selection == "*" or selection == "/" or selection == "//" or selection == "%" or selection == "**"):
            num1 = int(input("Please Enter an Integer: "))
            num2 = int(input("Please Enter an Integer: "))
            luckyCalculator(num1, num2, selection)
        else:
            print("Error! Wrong Input!")

    elif (choose == "l" or choose == "L"):
        range1 = int(input("Please Enter an Integer: "))
        range2 = int(input("Please Enter an Integer: "))
        luckyNumber(range1, range2)

    elif (choose == "q" or choose == "Q"):
        print("Goodbye!")

    else:
        print("Error! Wrong Input.")

if __name__ == "__main__":
    main()
