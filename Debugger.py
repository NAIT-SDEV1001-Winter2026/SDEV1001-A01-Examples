#Using the python Debugger
#n - next line of code
#l - list surrounding lines of code
#ll - lists more surrounding lines of code
#c - continue until the end of the program OR the next breakpoint()
number1 = 5
number2 = 8

breakpoint()#enter breakpoint mode here

answer = number1 + number2
print(f"The sum of {number1} and {number2} is {answer}")

breakpoint()
if answer < 10:
    print("over 10")
else:
    print("not over 10")
