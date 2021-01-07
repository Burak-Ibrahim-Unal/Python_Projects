from turtle import *

def rectangle(a,b,w,pc,f):
    width(w)
    pencolor(pc)
    fillcolor(f)
    begin_fill()
    i=0
    for i in range(2):
      fd(a)
      lt(90)
      fd(b)
      lt(90)
    end_fill()
rectangle(100,200,10,"blue","yellow")