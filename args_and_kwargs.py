#function to add 2 numbers together and return the sum
def  add_numbers (number1, number2):    
    answer = number1 + number2
    return answer

# print(add_numbers(5,3))

#good! but you can only add 2 numbers
#what if you wanted this?

#print(add_number(5,7,3,8,5,2))

#use *args to perform this task
# A *args parameter allows an variable number of values to be passed it. They values passed to it are stored in a Tuple. The * in the param name means it is an arg parameter, but the name does not have to be args.
# use **Kwargs for key-value pair data (ditionary data)
# Kwargs store a key (string) and a value

def add_any_numbers(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(add_any_numbers(5,3,3,6,8,7,3,4,8,77,55,33,22,55,4343,65))

# * placed in front of a collection (not a parameter) is called the unpacking operator. It will return all the values seperately

grades = (66,76,46,88,65)
print (grades)

print (*grades)

print("Shane")
print(*"Shane")

#Create a function to will:
    #have a sport parameter and display that sport
    #have a parameter for a number of scores and display them
    #have a parameter for different coaching positions and display them

def sport_stuff(sport,*scores,**staff):
    print (f"The sport is: {sport}")

    print("Scores:")
    for score in scores:
        print (score)

    print("Staff:")
    for key, value in staff.items():#loop through all the key value pairs (dictionary) in the kwarg
        print(f"- {key}: {value}")
    

sport_stuff("Soccer",3,5,2,7,7,4, coach = "Yoda", assistant_coach = "Luke Skywalker", water_boy = "Homer")


