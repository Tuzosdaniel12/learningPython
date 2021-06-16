#imports      
from Cars import Car
from Dealership import Dealership

my_dealership = Dealership()

#create cars
my_car_one = Car("Model T", 1908)
my_car_two = Car( "Phantom", 2020, "Rolls Royce")

#add car to delership
my_dealership.add_car(my_car_one) 
my_dealership.add_car(my_car_two)

num = 1
print("\n====DEALERSHIP====")
for car in my_dealership:
    print(f"----Car {num}----")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Year: {car.year}")
    car.go("Fast")
    car.stop()
    car.go("Fast")
    num+=1

print("\n====MY CARS====")
print(my_car_two)
print(my_car_one)


if my_car_one == my_car_two:
    print("equal")
else:
    print("not equal")
#type of 
    # print(type(my_car_one))
#check if is an instance
    # print(isinstance(my_car_one, Car))