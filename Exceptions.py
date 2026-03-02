#try/except
#Handle unexpected situations gracefully and prevent the code from crashing
#try - if an exception occurs in the try block, it will jump to the except block
#Except - addresses the exception and outputs a nice error message
# try:
#     numerator = int(input("enter the numerator: "))
#     denominator = int(input("enter the denominator: "))

#     quotient = numerator/denominator

#     print (quotient)
# except:
#     print("Something went BOOM!")

#The above code works, but the error message is vague. We would like to be as specific as possible so they user does not make the same error twice!
# try:
#     numerator = int(input("enter the numerator: "))
#     denominator = int(input("enter the denominator: "))

#     quotient = numerator/denominator

#     print (quotient)

# except ValueError:
#     print("You did not enter an integer! Try again!")
# except ZeroDivisionError:
#     print("Remember grade 3? You cannot divide by 0!")
# except:
#     print("Something went BOOM!")

# print ("Have a groovy day!")

#Show a nice error message AND the Python (ugly) error message
# try:
#     numerator = int(input("enter the numerator: "))
#     denominator = int(input("enter the denominator: "))

#     quotient = numerator/denominator

#     print (quotient)

# except ValueError as error_message:
#     print(f"You did not enter an integer! Try again! ({error_message})")
# except ZeroDivisionError as error_message:
#     print(f"Remember grade 3? You cannot divide by 0! ({error_message})")
# except Exception as error_message :
#     print(f"Something went BOOM! ({error_message})")
# finally:
#     print("Always Execute!")#Executes if try succeeds or fails

# print ("Have a groovy day!")

#Best practices
#Keep the try blocks as small as possible
#Provide detailed and nice error messages
#Trap specific exceptions where possible

#ValueError - int("Turkey")
#ZeroDivisionError - 6/0
#NameError - print (answer) - There is no variable answer
#TypeError - len(42) - len is for strings not integers

#Try/Except validation loops
#loop until the user enters an integer
# while True:
#     try:
#         user_input = int(input("Enter an integer: "))
#         break
#     except ValueError:
#         print("That is not an integer! Try again!")
    
# print("Have a groovy day!")

#Must enter an integer between 1 and 10. Display different error messages for not in integer and not between 1 and 10. Loop until valid
# while True:
#     try:
#         user_input = int(input("Enter an integer: "))
#         if user_input >=1 and user_input <=10:
#             break
#         else: 
#             print("That is not between 1 and 10!")
#     except ValueError:
#         print("That is not an integer! Try again!")
    
# print("Have a groovy day!")

#Same as above but in both error messages display the value the user entered(that was wrong)
while True:
    try:
        user_input = input("Enter an integer: ")
        user_number = int(user_input)
        if user_number >=1 and user_number <=10:
            break
        else: 
            print(f"{user_number} is not between 1 and 10!")
    except ValueError:
        print(f"{user_input} is not an integer! Try again!")
    
print("Have a groovy day!")

#Summary
#Try the risky operation
#If it explodes , catch it in the except
#If it works, exit the loop

#For your assignment you could use try/except(and possibly other techniques) for:
    #Catching Casting errors from user input (ValueError)
    #Accessing an index that is not in a list (IndexError)
    #Remove an item with remove() from a list that is not there (ValueError)
