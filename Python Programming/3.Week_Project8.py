from turtle import *

# Çokgen Çizimi


def drawing(side,size,color):
    width(3);
    pencolor("blue");
    fillcolor(color);
    begin_fill();
    for i in range(sides):
        fd(size);
        lt(360/sides);
    end_fill()

sides= int(input("Number of sides:"));
size= int(input("Number of size:"));
color = input("Color:");
drawing(sides,size,color);