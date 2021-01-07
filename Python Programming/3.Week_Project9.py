from turtle import *

# Çokgen Çizimi

def rectangle(a,b,c):
    pencolor("blue")
    pensize(2);
    fillcolor(c)
    begin_fill()
    for i in range(2):
        fd(a)
        left(90)
        fd(b)
        left(90)
    end_fill()
def triangle(a,col):
    pencolor("blue")
    pensize(2)
    fillcolor(col)
    begin_fill()
    for i in range(3):
        fd(a)
        lt(120)
    end_fill()

rectangle(90,120,"yellow")
goto(0, 120)
triangle(90,"red")