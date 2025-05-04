# Arbish Ali Mohbani                    02/12/2025
# Lab # 3 
# The perimeter of a rectangle is the total distance covered by its boundaries or the sides. Since there are four sides of a rectangle, thus, the perimeter of the rectangle will be the sum of all four sides.
# https://byjus.com/maths/perimeter-of-rectangle/
# Author: Not mentioned, Published Date: Not mentioned, Access Date: 02/11/2025

def rectanglePerimeter(length, width):
    perimeter = 2*(length+width)
    return perimeter


def main():
    num1 = float(input("Enter the value of length: "))
    num2 = float(input("Enter the value of width: "))
    num3 = rectanglePerimeter(num1, num2)
    print("The perimeter of the rectangle is: "+str(num3))


if __name__ == "__main__":
    main()

# End