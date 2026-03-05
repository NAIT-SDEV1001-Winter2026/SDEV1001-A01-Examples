#functions are a bunch of code that is given a name
#called by their name
#Can return values
#Values passes to functions when they are called are called arguments and the arguments are accepted by parameters
#Parameters are not optional
#Breaks down large problems into smaller problems

# name = input("Enter your name: ")
# print (f"Welcome {name}")

#Using functions 

def get_name():
    name = input("Enter your name: ")
    return name

def display_name(name):
    print  (f"Welcome {name}")

name = get_name()
display_name(name)

#Mutiple parameters
def add_numbers (number1, number2):
    answer = number1 + number2
    return answer

print(add_numbers(5,3))

#not optional
# print(add_numbers())

#default values for parameters
def display_favorite_color(color = "Yellow"):
    print(f"Your favorite color is {color} ")

display_favorite_color()
display_favorite_color("Blue")

