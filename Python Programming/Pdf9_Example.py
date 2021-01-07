class Vector:
    def __init__(self,a,b):
        self.A1=a
        self.B1=b

    def __add__(self, other):
        return Vector(self.A1+other.A1,self.B1+other.B1)

    def __str__(self):
        return 'Vector (%d,%d)' %(self.A1,self.B1)

V1=Vector(2,5)
V2=Vector(-1,2)
print(V1+V2)

#-----------------------------------------------------------
'''class Foo():
    def _init_(self):
        self.l = [{"Susan": ("Boyle", 50, "alive")}, {"Albert": ("Speer", 106, "dead")}]

    def _str_(self):
        ret_str = ""
        for d in self.l:
            for k in d:
                ret_str += "".join([k, " ", d[k][0], " is ", str(d[k][1]), " and ", d[k][2], ". "])
        return ret_str


foo = Foo()
print(foo)'''