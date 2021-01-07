from turtle import *

def DrawNgon(side,length,color):
    pensize(3)
    fillcolor(color)
    pencolor("blue")
    begin_fill()
    for i in range(side):
        fd(length)
        rt(360/side)
    end_fill()

s=int(input("Please input side number:\n"))
l=int(input("Please input length:\n"))
c=input("Please enter color:\n")

DrawNgon(s,l,c)
exitonclick()