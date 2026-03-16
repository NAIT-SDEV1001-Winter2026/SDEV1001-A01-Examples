def add(number1,number2):
    answer = number1 + number2
    return answer

def subtract(number1,number2):
    answer = number1 - number2
    return answer

def multiply(number1,number2):
    answer = number1 * number2
    return answer

def divide(number1,number2):
    answer = number1 / number2
    return answer
#main guard
#__name__ is a dunder variable that is populated by Python
#If this py file is run directly, __name__ contains "__main__"
#If this py file is not run directly(imported) it contains the name of the file it is in
print(__name__)
if __name__ == "__main__":
    #Demonstrate Functions
    print(add(6,3))
    print(subtract(6,3))
    print(multiply(6,3))
    print(divide(6,3))


