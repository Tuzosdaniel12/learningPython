class Car:
    wheels = 4
    doors = 2
    engine = True 
    #contructor
    def __init__(self, model, year, make="Ford"):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False
    #convert object into string
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model 
        
    #behavior methods
    def stop(self):
        if self.is_moving:  
            print("The car has stopped")
            self.is_moving = False
        else:
            print("The car has already stopped")

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print("The start moving")
                self.is_moving = True
            print(f"The car is going {speed}")
        else:
            print("You have run out of gas")
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        return True

