#And/Or
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

#AND
#All condition must be true for the entire condition to be true
if number1 == 5 and number2 == 8:
    print("Number 1 is 5 AND number 2 is 8")
#OR
#If any of the conditions are true, the entire condition is true
if number1 == 5 or number2 == 8:
    print ("At least one of the conditions are true")