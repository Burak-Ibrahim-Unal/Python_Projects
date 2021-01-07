import turtle
""" Burak Ibrahim Unal Python Homework """

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(750,450)
screen.update()
f_speed = 400
b_speed= 800
t_speed = 200

# To control the movement of our "turtle"
def forward():
  image1 = "fishR.gif"
  screen.addshape(image1)
  turtle.shape(image1)  
  turtle.forward(f_speed)
  
def backward():
  image2=  "fishL.gif"
  screen.addshape(image2)
  turtle.shape(image2)  
  turtle.backward(b_speed)

def left_side():
  image2=  "fishL.gif"
  screen.addshape(image2)
  turtle.shape(image2)  
  turtle.left(t_speed)

def right_side():
  image1 = "fishR.gif"
  screen.addshape(image1)
  turtle.shape(image1)
  turtle.right(t_speed)

turtle.speed(2)
turtle.penup()
turtle.home()

for i in range(10):

    forward()
    #left()
    backward()
    forward()
    #right()

input()
