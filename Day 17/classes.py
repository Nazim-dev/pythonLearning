class Vehicle:
    
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.seats = 4

    def enter_race_mode(self):
        self.seats = 2

car = Vehicle("Toyota", 2015)

car.enter_race_mode()
print(car.brand, car.seats)