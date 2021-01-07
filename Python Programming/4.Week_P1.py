from turtle import *
from random import randint,random


def axisX():
    up()
    goto(-200,-125)
    down()
    fd(400)
    lt(160)
    fillcolor("black")
    begin_fill()
    fd(20)
    lt(110)
    fd(15)
    lt(110)
    fd(20)
    end_fill()
    x=-165
    y=-125
    for i in range(5):
        up()
        goto(x,y-20)
        down()
        write(chr(65+i))
        x+=70

def axisY():
    up()
    goto(-200,-125)
    down()
    lt(70)
    fd(290)
    lt(160)
    fillcolor("black")
    begin_fill()
    fd(20)
    lt(110)
    fd(15)
    lt(110)
    fd(20)
    end_fill()
    rt(20)
    x=-200
    y=-125
    for i in range(10):
        up()
        y+=25
        goto(x-5,y)
        down()
        goto(x+5,y)
        up()
        goto(x-25,y-7)
        write((i+1)*10)
    goto(x-25,y+15)
    write("%")

def bar(xpos,height):
    up()
    goto(-200+xpos,-125)
    down()
    fillcolor(random(),random(),random())
    begin_fill()
    for i in range(2):
        fd(height)
        rt(90)
        fd(70)
        rt(90)
    end_fill()

def barchart():
    setup(500,350)
    title('Barchart')
    ht()
    x=0
    axisX()
    axisY()
    for i in range(5):
        y=randint(0,250)
        bar(x,y)
        x+=70


barchart()
input()