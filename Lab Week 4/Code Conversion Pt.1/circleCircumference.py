# Arbish Ali Mohbani                    02/12/2025
# Lab # 3 

import math

def circleCircumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def main():
    num1 = float(input("Enter the radius of the circle: "))
    num2 = circleCircumference(num1)
    print("The circumference of the circle is: "+str(num2))


if __name__ == "__main__":
    main()





# End