#Decision making is the ability to control the flow of a program based on conditions
#In Python we will use if , elif, else statements

#Syntax of a basic if decision
#if condition:
    #code to run if the condition is True

#Comparison Operators: ==, !=, <, <=, >, >=

# age = 11

# if age >= 18:
#     print("You are an adult!")#only if age >=18
#     print("Start paying the bills!")#only if age >=18

# print("Have a groovy day!")# Always

# #== comparison
# score = 100

# if score == 100:    
#     print("Perfect Score!")

# #ask the user for their name. If it is Your name print "Awesome Name!"
# name = input("Enter your name: ")

# if name == "Shane":
#     print ("Awesome Name!")

# print("Have a groovy day!")

# #Remember, strings are case sensitive. Shane is different than shane
# #In this course, it will be an expectations that user entered strings will be tested as case insensitive(user can enter any case)
# if name.upper() == "SHANE":
#     print (f"{name.capitalize()} is an awesome Name!")

# print("Have a groovy day!")

#Boolean
#Use the word is in front of Boolean variable names
# is_awesome = True

# if is_awesome == True:
#     print("Awesome!")

# #Boolean conditions should be written as
# if is_awesome:#is_awesome is already True or False 
#     print("Awesome!")

# #NOT
# if not is_awesome:#if is_awesome is False
#     print("Not awesome :(")

# #if else
# #if condition: 
#     #True code
# #else:
#     #False code

# grade = int(input("Enter your grade: "))
# #With just if statements
# #BAD :( :(
# if grade >=50:
#     print("Pass")
# if grade <50:
#     print("Fail")

# print ("Have a groovy day!")

# #GOOD WAY :)
# if grade >=50:
#     print("Pass")#If condition is true
#     print("Good work!")
# else:
#     print("Fail")#If condition is false
#     print("Keep Trying!")

# print ("Have a groovy day!")

#if elif else
grade = int(input("Enter your grade: "))

if grade >=80:
    print ("Honors!")
    print ("You are smart!")
elif grade >=50:
    print ("Pass")
elif grade == 0:
    print("Where were you?")
else:
    print("Fail")














