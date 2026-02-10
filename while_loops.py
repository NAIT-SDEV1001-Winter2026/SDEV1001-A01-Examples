#While loops repeat a block of code while a condition is true
#useful when you don't know how many times to loop

#Counter Controlled Loop
#Count up to 5
counter = 1

while counter <=5:#Keep looping while this condition is True
    print(f"Number: {counter}")
    counter += 1#Increment the counter (IMPORTANT!)

#User controlled Loop
#Ask for numbers to add. Enter 'done' to print the sum

total = 0
while True: #An endless loop unless break
    value = input("Enter a number. done to quit: ")
    if value.lower() == "done":
        break
    total +=int(value)
print (f"Sum: {total}")

#Using a boolean variable
keep_going = True
while keep_going:
    answer = input("Would you like to conitnue?(n): ")
    if answer.lower() == "n":
        keep_going = False
print ("Loop over!")


