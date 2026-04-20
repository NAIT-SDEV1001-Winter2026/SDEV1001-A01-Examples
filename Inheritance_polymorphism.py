 #Parent class which will be inherited by all the child classes

#Parent Class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"This is a {self.make}, {self.model}"
    
#Child class that inherits from the Vehicle class
#Add additional attributes for an Airplane
class Airplane(Vehicle):
    #Override the constructor to create attributes specific to Airplanes
    #Long way(DO NOT USE)
    # def __init__(self, make, model, props, flaps):
    #     self.make = make
    #     self.model = model
    #     self.props = props
    #     self.flaps = flaps

    #BETTER WAY. USE THIS
    def __init__(self, make, model, props, flaps):
        super().__init__(make,model)#use the make and model attributes from the parent (Vehicle)
        self.props = props
        self.flaps = flaps

    #This method is in the parent class as well. It will use the more local version(this one)
    def __str__(self):
        return f"This is a {self.make}, {self.model} with {self.props} props" 
    
    def move(self):
        print("flies from here to there")


my_airplane = Airplane("Cesna","A123", 2, True)
print(my_airplane)

class Boat(Vehicle):
    def __init__(self, make, model, horsepower):
        super().__init__(make,model)
        self.horsepower = horsepower  

    def move(self):
        print("floats from here to there")  

my_boat = Boat("IDK","lol",50)
print(my_boat)

#create a new child class for Motorcyles
#inherit from vehicle and add 2 addtional attributes related to motorcycles only
#override __str__ to display ALL the attributes

class Motorcycle(Vehicle):
    def __init__(self, make, model, sidecar, enginepower):
        super().__init__(make, model)
        self.sidecar = sidecar
        self.enginepower = enginepower

    def __str__(self):
        return f"This is a {self.make}, {self.model}. It {"has" if self.sidecar else "does not have"} a side car and has {self.enginepower} horsepower"
    
    def move(self):
        print("Zooms from here to there")

my_motorcyle = Motorcycle("Harley", "Hog", True, 500)
print(my_motorcyle)

#Polymorphism
#The same method in different classes that gives different results/behavious

print("\n\nPolymorphism")
my_airplane.move()
my_boat.move()
my_motorcyle.move()

for vehicle in (my_airplane,my_boat,my_motorcyle):
    vehicle.move()






    
