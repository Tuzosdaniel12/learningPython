class Dealership:
    #constructor
    def __init__(self):
        self.cars = []
    #tells python to iterate 
    def __iter__(self):
        yield from self.cars
    #behavior
    def add_car(self, car):
        self.cars.append(car)