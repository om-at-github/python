# python class_Vehicle_inheritance.py

# Create classes Vehicle, Car, and Truck where Car and Truck inherit from Vehicle.
#  Write a function get_vehicle_info(obj) that prints "Car" if obj is an instance 
# of Car, "Truck" if obj is an instance of Truck, and "Unknown Vehicle" otherwise.
#  Use isinstance and issubclass to determine the type.

class Vehicle:
    def __init__(self, name, color, wheels, doors, seats, engine, transmission):
        self.name = name
        self.color = color
        self.wheels = wheels
        self.doors = doors
        self.seats = seats
        self.engine = engine
        self.transmission = transmission

class Car(Vehicle):
    def __init__(self, name, color, wheels, doors, seats, engine, transmission):
        print("________d")
        
class Truck(Vehicle):
    def __init__(self, name, color, wheels, doors, seats, engine, transmission):
        def get_vehicle_info(self):
            if isinstance(self, Car):
                print("Car")
            elif isinstance(self, Truck):
                print("Truck")

my_Vehicle = Vehicle
my_Vehicle.get_vehicle_info()