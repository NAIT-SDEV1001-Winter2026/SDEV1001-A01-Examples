#There are a number of methods that can be used with lists

#Sorting
numbers = [42,7,19,100,3]
numbers.sort() #sorts ascending
print (numbers)

numbers.sort(reverse = True)# Sort Descending
print (numbers)

#Add to a list (single value)
colors = ["red","blue"]
colors.append("green")#appends to end of the list a single value
colors.insert (1,"yellow")#insert at an index. Values are moved down to make room
print(colors)

#Append a list to another list
colors.extend(["pink","purple"])#extends this list to the colors list
print(colors)

#removing values
#pop (by index) AND returns the value removed
pets = (["cats","lizards","ferrets","birds","anaconda"])
pets.pop(1)#removes the value at index 1. The return value does not need to be used
print(pets)

removed = pets.pop(2) 
print(removed)

#remove by value
pets.remove("cats")
print (pets)

cities = ["Edmonton", "Calgary", "Toronto", "Red Deer"]
print (f"Is Calgary in the list? {"Calgary" in cities}")

check_city = input("Enter a city: ")
result = check_city in cities#True if check_city is in the cities list
if result:
    print("Found it!")

#index of a value
print(f"The index for Calgary is: {cities.index("Calgary")}")

#Count the occurences of a value in a list
cities = ["Edmonton", "Calgary", "Toronto", "Red Deer", "Edmonton"]
print(f"Edmonton is in the list {cities.count("Edmonton")} times")

#Clear a list
cities.clear()
