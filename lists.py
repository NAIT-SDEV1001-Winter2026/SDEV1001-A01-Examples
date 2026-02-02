#A list is a collection of values stored in a single variable
#Each value can be accessed by a zero based index
#Can hold different datatypes (including other lists)

colors = ["red", "blue", "green", "yellow"]
#display the list
print(colors)

#access a single value by its index
print(colors[1])
#Access from the end of the list
print(colors[-1]) #Yellow

#change a value
colors[2] = "purple"
print (f"green is now {colors[2]}")

#slicing lists
#the lower boundary is inclusive, upper boundary is exclusive
#first three colors
print (colors[0:3])

#length of a list
print(len(colors))

#accessing a list outside its boundaries is an error
print(colors[85])
