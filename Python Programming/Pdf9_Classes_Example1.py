import math

class Circle:
    def __init__(self,radius=1):
        self.r=radius
    def perimeter(self):
        return 2*self.r*math.pi
    def area(self):
        return 2*math.pow(self.r,2)*math.pi
    def setRadius(self,radius):
        self.r=radius
    def getRadius(self):
        return self.r

c1=Circle()
c1.setRadius(3)
print("The circle with radius 3 area is:{} and perimeter is:{}\n".format(float("%0.2f"%c1.area()),float("%0.2f"%c1.perimeter())))

c2=Circle(6)
print("The circle with radius 3 area is:{} and perimeter is:{}\n".format(float("%0.2f"%c2.area()),float("%0.2f"%c2.perimeter())))

