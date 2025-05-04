# Arbish Ali Mohbani                02/12/2025
# Lab # 3 
# Matthew Holman
# https://www.geeksforgeeks.org/draw-any-polygon-in-turtle-python/
# https://www.geeksforgeeks.org/turtle-setpos-and-turtle-goto-functions-in-python/

import turtle

def tridecagonTurtle(s1, x1, y1):
    t = turtle.Turtle()
    turtle.setpos(x1, y1)
    for i in range(0, 13):
        turtle.forward(s1)
        turtle.right(360/13)

    turtle.done()

def main(): 
    s = int(input("Enter the length of one of the sides: "))
    x = int(input("Enter the x-coordinate of the vertex point: "))
    y = int(input("Enter the y-coordinate of the vertex point: "))
    tridecagonTurtle(s, x, y)   
    

if __name__ == "__main__":
    main()