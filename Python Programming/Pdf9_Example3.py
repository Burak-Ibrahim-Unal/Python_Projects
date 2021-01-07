class MyVector(object):
    def __init__(self,x,y):
        self.X1=x
        self.Y1=y

    def get_x(self):
        print("Return X:{}".format(self.X1))
        return self.X1

    def set_x(self,x):
        print("Set X:{}".format(x))
        self.X1=x
    def get_y(self):
        print("Return Y:{}".format(self.X1))
        return self.Y1

    def set_y(self,y):
        print("Set Y:{}".format(self.X1))
        self.Y1=y

    x=property(get_x,set_x)
    y=property(get_y,set_y)

v1=MyVector(3,2)
x=v1.x
v1.x=4
y=v1.y
v1.y=5

print("X:{} and V1.X:{} and Y:{} and  V1.Y:{}".format(x,v1.x,y,v1.y))