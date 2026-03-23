#Object Oriented Programming (OOP)
#OOP is a style where we model, in code, real world things using classes
#A class is like a blueprint. Objects are created(instantiated) from the class(blueprint)

#Example:
#Class - Car
#Object - one specific car (Ford F150)

#Car class
class Car:

    #Constructor method - It is called __init__
    #Runs automatically when an object is created from the class
    #self refers to the current object being instantiated(created)
    #self must be the first parameter
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #__str__ is a method that is called whenever an object is converted to a string to print. 
    #We can override that behaviour to print what we want instead
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"
    
    #__repr__ is like __str__ BUT it only is called automatically from certain environments    
    #Used more for testing in those environments
    def __repr__(self):
        return f"{self.make}, {self.model}, {self.year}"

    #Override the __eq__ to specify HOW objects are compared
    #return True if all the attributes are the same in both objects being compared
    def __eq__(self,other):
        return self.make == other.make and self.model == other.model and self.year == other.year

#Mainline
#Create a car object(an instance of the car class)
if __name__ == "__main__":
    car1 = Car("Honda", "NSX", 2001)

    print(car1.make)
    print(car1.model)
    print(car1.year)

    car2 = Car("Kia", "Sportage", 2015)
    print (car2.make)

    #change an attribute
    car2.year = 2016
    print(car2.year)

    #List of cars
    cars = [car1,car2]
    print("cars in a list:")
    for car in cars:
        print(f"{car.make}, {car.model}, {car.year}")

    #print a car object
    #without overriding __str__ , printing an object prints its memory location. Not usefull!
    #Override __str__ to return what we want to print
    print(car1)
    print(car2)
    #using the new __str__ method to print the attributes of all the cars
    for car in cars:
        print(car)

    #comparing objects
    test_car1 = Car("Volkswagon", "Beatle", 1964)    
    test_car2 = Car("Volkswagon", "Beatle", 1964)    
    #By default, you are comparing the memory locations of these 2 objects
    #Therefore these are not equal
    #Override the __eq__ method to change how the objects are compared
    if test_car1 == test_car2:
        print("same")
    else:
        print("not same")



















