#Ozgur Ucar - Assignment: Module 3 Lab - Case Study: Lists, Functions, and Classes

"""
This code defines a simple Python program with a Vehicle class and a derived Automobile class.
The program specifies a vehicle type and gathers information about a car, such as the year, make, model, number of doors, and roof type, based on user input. 
The Automobile class inherits from the Vehicle class, gaining the vehicle type attribute, and adds attributes specific to automobiles.
An Automobile object is created with the provided information, and the details of the car are then printed on the screen.
"""

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

# Gathering user input
vehicle_type = "car"
year = input("Enter the year of the car: ")
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Creating an Automobile object with the provided input
car = Automobile(vehicle_type, year, make, model, doors, roof)

print("\nHere is the information about the car you entered:")
car.display_info()
