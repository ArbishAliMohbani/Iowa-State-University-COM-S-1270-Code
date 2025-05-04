# Arbish Ali Mohbani                02/22/2025
# Lab # 5 
# Matthew Holman
# https://www.geeksforgeeks.org/draw-any-polygon-in-turtle-python/
# https://www.geeksforgeeks.org/turtle-setpos-and-turtle-goto-functions-in-python/

import turtle

def drawMultipleTridecagons(s, x, y, nr, sr):
    t = turtle.Turtle()
    for j in range(0, nr):
        turtle.setpos(x, y)
        for i in range(0, 13):
            turtle.forward(s)
            turtle.right(360/13)
        x+=sr
    turtle.done()

def main(): 
    s = int(input("Enter the length of one of the sides: "))
    x = int(input("Enter the x-coordinate of the vertex point: "))
    y = int(input("Enter the y-coordinate of the vertex point: "))
    nr = int(input("Enter how many Tridecagons you want: "))
    sr = int(input("Enter the amount of space you want between Tridecagons: "))
    drawMultipleTridecagons(s, x, y, nr, sr)   
    

if __name__ == "__main__":
    main()