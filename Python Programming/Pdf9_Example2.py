class Person:
    def __init__(self):
        self.pets=[]

    def add_pet(self,pet):
        self.pets.append(pet)


Burak=Person()
Cem=Person()
Burak.add_pet("Cat")
Burak.add_pet("Monkey")
Cem.add_pet("Donkey")

print (Burak.pets)
print(Cem.pets)
#------------------------------------
