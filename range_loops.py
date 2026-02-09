# #Review
# #strings are lists of single characters
# # "abc"
# # ["a","b","c"]

# #Loop through a string and print each letter on its own line
# string = "Have a groovy day!"
# for letter in string:
#     print(letter)

# #Ask the user for a string and print out how many vowels are in the string
# #Enter a string: Happy Monday!
# #There are 3 vowels in 'Happy Monday'

# string  = input("Enter a string: ")

# vowels = ("a","e","i","o","u")
# count = 0

# for letter in string:
#     if letter.lower() in vowels:
#         count += 1
# print(f"There are {count} vowels in {string}")

#Range Loops
#range() generates a sequence of numbers and can be used for a loop counter
#Syntax
#range (start, stop, step)
#start is inclusive, stop is exclusive

#print numbers 1 to 5
for number in range(1,6):
    print(f"Number: {number}")  

#calculate and print the cubes of numbers from 0 to 4
#0 cubed is 0
#1 cubed is 1

for number in range(0,5):
    print (f"{number} cubed is {number ** 3}")

#If your range starts at 0, you can omit the start value
for number in range(5):
    print (f"{number} cubed is {number ** 3}")

#print the even numbers between 4 and 20
for number in range(4,21,2):
    print (number)

#Ask the user for how many "Hello World" to print and print that many on seperate lines
how_many = int(input("How many 'Hello World' to print? "))

for count in range (0,how_many):
    print ("Hello World")

#Print a string a certain number of times on the same line
print ("Hello " * 8)

#Ask the user for how many rows of a right angle triangle to print:
#How many rows: 4
#*
#**
#***
#****

how_many = int(input("How many rows? "))
for count in range (how_many):
    print("*" * (count + 1) )










