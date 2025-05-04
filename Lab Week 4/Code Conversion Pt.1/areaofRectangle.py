# Arbish Ali Mohbani                02/12/2025
# The area of any rectangle is calculated, once its length and width are known. By multiplying length and breadth, the rectangle’s area will obtain in a square-unit dimension.
# https://byjus.com/maths/area-of-rectangle/#:~:text=of%20a%20Rectangle-,Area%20of%20a%20Rectangle,in%20a%20square%2Dunit%20dimension
# Author: Not mentioned, Published Date: Not mentioned, Access Date: 02/11/2025

def areaofRectangle(height, base):
    num3 = height*base  
    return num3  

def main():
    num1 = float(input("Enter the height value: "))
    num2 = float(input("Enter the base value: "))
    area = areaofRectangle(num1, num2)
    print("This is the area of rectangle: "+str(area))

if __name__ == "__main__":
    main()

#End