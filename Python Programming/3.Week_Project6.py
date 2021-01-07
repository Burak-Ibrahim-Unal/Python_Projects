from turtle import *

# Kare Çizimi

def square(color):
    pensize(3)
    pencolor("red")
    fillcolor(color)
    begin_fill()
    i=0
    while i<4:
      forward(100)
      left(90)
      i+=1
    end_fill()


def drawing(angle):
    rt(angle)
    square("blue")
    rt(angle)
    square("yellow")
    rt(angle)
    square("red")
    rt(angle)
    square("green")
    rt(angle)
    square("orange")
    rt(angle)
    square("purple")
    """begin_fill();
    for i in range(5):
        fd(100);
        lt(108);
    end_fill()"""

#square("blue")
drawing(60)
exitonclick()