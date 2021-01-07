from turtle import *



def spiral1(step):
    p=10
    x=1
    while (x<step):
        fd(p)
        rt(90)
        p=p+10
        x=x+1

def spiral2(step):
    if (step<10): return
    fd(step)
    rt(90)
    step=step-5
    spiral2(step)


def main():
    spiral1(20)
    up()
    goto(-70,80)
    down()
    spiral2(250)
main()
exitonclick()