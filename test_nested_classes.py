class Car:
    brand=""
    model=""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Person:
    age=0
    name=""
    car=None
    def __init__(self, age, name, car):
        self.age = age
        self.name = name
        self.car = car

x = Person(age=33, name="Pedro", car = Car(brand="renault", model="clio"))
print(x)
print(x.name)
print(x.age)
print(x.car)
print(x.car.brand)
print(x.car.model)