def add(*args):  # allows to use unlimited parameter in it
    total = 0
    for n in args:
        total += n
    print(total)


add(2, 5, 4, 12, 3)

def calculate(n,**kwargs):
    print(kwargs)
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)
    n+= kwargs["add"]
    n*=kwargs["multiply"]
    print(n)


calculate(2,add=3,multiply=5) # {'add': 3, 'multiply': 5} dictionary 25 (2+3) *5

class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model= kw.get("model")
        self.seats= kw.get("seats")

my_car=Car(model="Prius",seats=4)


print(my_car.seats)