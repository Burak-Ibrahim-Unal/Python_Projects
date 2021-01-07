from turtle import *
from turtle import Turtle
from random import randint

setup(900,300)
t0=Turtle()
t1=Turtle()
t2=Turtle()
t3=Turtle()

t0.ht()
t1.ht()
t2.ht()
t3.ht()

t0.pu()
t0.goto(-310,50)
t0.write('Start')
t0.goto(-300,40)
t0.down()
t0.goto(-300,-40)

t0.pu()
t0.goto(190,50)
t0.write('Stop')
t0.goto(200,40)
t0.down()
t0.goto(200,-40)

t1.color("red")
t2.color("green")
t3.color("Blue")

t1.shape('turtle')
t2.shape('turtle')
t3.shape('turtle')

t1.pu()
t1.goto(-310,30)
t1.down()
t1.st()

t2.pu()
t2.goto(-310,0)
t2.down()
t2.st()

t3.pu()
t3.goto(-310,-30)
t3.down()
t3.st()


def game():
    x1=x2=x3=step=0
    while True:
        a=randint(1,30)
        b=randint(1,30)
        c=randint(1,30)
        x1 += a
        x2 += b
        x3 += c
        step += 1
        t1.fd(a)
        t2.fd(b)
        t3.fd(c)
        if x1>=500 or x2>500 or x3 >=500:
            t0.ht()
            t0.up()
            t0.goto(-100,-70)
            if x1>x2 and x1>x3:
                t0.pencolor("red")
                t0.write("Red Won",font=("Arial",18,"normal"))
            if x2>x1 and x2>x3:
                t0.pencolor("green")
                t0.write("Green Won",font=("Arial",18,"normal"))
            if x3>x1 and x3>x1:
                t0.pencolor("blue")
                t0.write("Blue Won",font=("Arial",18,"normal"))
            break
game()
input()