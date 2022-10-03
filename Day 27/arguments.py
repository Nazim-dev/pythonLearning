def add(*args):
    total = sum(args)
    return total


print(add(8,5,2,1))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n -= kwargs["subtract"]
    print(n)


calculate(1, add=20, subtract=3)

class Car:
    
    def __init__(self, **kw):
        self.make = kw.get["make"]
        self.model = kw.get["model"]

toyota = Car(make="Toyota", model="Corolla")

print(toyota.make)