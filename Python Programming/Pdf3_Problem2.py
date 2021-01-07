from turtle import *

def rect(a,b,c):
    pensize(4)
    pencolor("blue")
    fillcolor(c)
    begin_fill()
    i=1
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)
    end_fill()

def triangle(a,c):
    pensize(4)
    pencolor("blue")
    fillcolor(c)
    begin_fill()
    i=0
    for i in range(3):
        fd(a)
        lt(120)
    end_fill()

def House2(a,b,c):
    rect(a,b,c)
    if a < b:
        goto(0, b)
        triangle(a, c)
    elif a > b:
        goto(0, b)
        triangle(a, c)

def House3(a,b,c):
    House2(a,b,c)
    House4(a,b,c)

def House4(a,b,c):
    rect(a,b,c)
    if a < b:
        goto(0, a)
        triangle(a, c)
    elif a > b:
        goto(0, b)
        triangle(b, c)

def polygon(side,size,color):
    width(3)
    pencolor("blue")
    fillcolor(color)
    begin_fill()
    for i in range(side):
        fd(size)
        lt(360/side)
    end_fill()




a=int(input("Rectangular edge length:\n"))
b=int(input("Rectangular other edge length:\n"))
c=input("Please type color to fill:\n")

House3(a,b,c)
exitonclick()

#rect(a,b,c)
"""if a<b:
    goto(0,b)
    triangle(a,c)
elif a>b:
    goto(0,b)
    triangle(a,c)"""

#polygon(a,b,c)
