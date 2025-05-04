# Arbish Ali Mohbani                    02/12/2025
# Lab # 3 

import math
def areaofCircle(radius):
    area = math.pi * (radius ** 2)
    return area


def main():
    num1 = float(input("Enter the radius of the circle: "))
    num2 = areaofCircle(num1)
    print("The area of the circle is: "+str(num2))

if __name__ == "__main__":
    main()



# End