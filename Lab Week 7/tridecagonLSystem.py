import turtle
import random

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        if i==3:
            startString+="/"
        endString = processString(startString, i)
        startString = endString

    return endString

def processString(oldStr, i):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch, i, oldStr)

    return newstr

def applyRules(ch, i, oldStr):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F'   # Rule 1
    elif ch == '/':
        newstr = "PH"
    else:
        newstr = ch    # no rules apply so keep the character
    print(i)
    return newstr

def tridecagonTurtle(newturtle, s1):
    for i in range(0, 13):
        newturtle.forward(s1)
        newturtle.right(360/13)

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == 'H':
            tridecagonTurtle(aTurtle, 50)
        elif cmd == 'P':
            aTurtle.penup()
            aTurtle.goto(random.randint(-200, 200), random.randint(-200, 200))
            aTurtle.pendown()
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
