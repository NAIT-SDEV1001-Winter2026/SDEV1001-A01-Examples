#try/except
#Handle unexpected situations gracefully and prevent the code from crashing
#try - if an exception occurs in the try block, it will jump to the except block
#Except - addresses the exception and outputs a nice error message
try:
    numerator = float(input("enter the numerator: "))
    denominator = float(input("enter the denominator: "))

    quotient = numerator/denominator

    print (quotient)
except:
    print("Something went BOOM!")