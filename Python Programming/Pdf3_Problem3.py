from turtle import *

pen(fillcolor="red", pencolor="blue", pensize=3)
for i in range(8):
    circle(30)
    pu()
    fd(50)
    rt(45)
    pd()

exitonclick()