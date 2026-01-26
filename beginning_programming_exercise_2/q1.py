# 1.	One acre of land is equal to 43,560 square feet. Write a program that asks the user to enter the number of acres and display the number of square feet.

# Output:
# Acre to Square foot converter. How many acres do you have? 25
# You have 25 acres which is equal to: 1089000 square feet

#1 acre = 43560 sq ft
CONVERSION_RATE = 43560
#get acres
acres = int(input("Acre to SQ feet converter. How many acres do you have? "))
#Calculate sq feet 
square_feet  = acres * CONVERSION_RATE
#print sq feet
print (f"You have {acres} acres which is equal to: {square_feet} square feet")

