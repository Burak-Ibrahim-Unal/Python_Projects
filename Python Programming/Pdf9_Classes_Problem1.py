import datetime

class Person:
    def __init__(self,name,surname,birthdate,email):
        self.Name=name
        self.Surname=surname
        self.Birth=birthdate
        self.Email=email

    def age(self):
        today=datetime.date.today()
        age=today.year-self.Birth.year
        if today<datetime.date(today.year,self.Birth.month,self.Birth.day):
            age-=1
        return age

p1=Person("Burak","Unal",datetime.date(1987,7,22),"burak@burak.com")
print("Name:{},Surname:{},Email:{},Birth:{},Age:{}".format(p1.Name,p1.Surname,p1.Birth,p1.Email,p1.age()))