numbers = [5,2,4,1,3]

print(f"Start: {numbers}")
list_length = len(numbers)

#Outer loop control # of passes
for start in range (0,list_length -1):
    swapped = False
    #go from the end of the list down to the start
    for index in range(list_length - 1,start,-1):
        if numbers[index-1] > numbers[index]:
            temp = numbers[index-1]
            numbers[index - 1] = numbers[index]
            numbers[index] = temp
            swapped = True
    if not swapped:
        break

print(f"Sorted: {numbers}" )