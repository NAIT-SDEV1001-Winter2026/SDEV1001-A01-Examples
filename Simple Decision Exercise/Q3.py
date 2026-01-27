# Question 3: Prompt for two numbers and display the highest value
# and whether it was the first or second number entered.
first = int(input("Enter number 1: "))
second = int(input("Enter number 2: "))

if first > second:
    print(f"The highest number between {first} and {second} is {first} and it was the first number entered!")
elif second > first:
    print(f"The highest number between {first} and {second} is {second} and it was the second number entered!") 
else:
    print("Both numbers are equal")
    
#OR
#code with just 2 prints
first = int(input("Enter number 1: "))
second = int(input("Enter number 2: "))

position = "same"

if first == second:
     print("Both numbers are equal.")     
elif first > second: 
    position = "first"
    highest = first
else:
    position = "second"
    highest = second

#OR
#code with just 2 prints
first = int(input("Enter number 1: "))
second = int(input("Enter number 2: "))

position = "same"

if first == second:
     print("Both numbers are equal.")     
elif first > second: 
    position = "first"
    highest = first
else:
    position = "second"
    highest = second

# #Solve so if they are equal, the equal message is printed and not the highest number message
# if position != "same":      
#     print(f"The highest number between {first} and {second} is {highest} and it was the {position} number entered!")

#OR we could say if both numbers are the same, then either number is the highest
first = int(input("Enter number 1: "))
second = int(input("Enter number 2: "))

position = "same"
highest = second

if first > second: 
    position = "first"
    highest = first
elif second > first:
    position = "second"
    
print(f"The highest number between {first} and {second} is {highest} and it was the {position} number entered!")