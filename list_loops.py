#For loops allow us to retrieve each value in a collection

bands = ["ABBA", "Journey", "Styx", "The Beatles"]

#loop through the list

for band in bands:
    print(f"{band} is a great band!")

#Enumerate function returns both the value AND the index
for index,band in enumerate(bands,start = 1):
    print(f"Band number {index} is {band}")

#Create list of 4 menu options.(add, update, delete,quit)
#1. Add
#2. Update
#3. Delete
#4. Quit

menu_options = ["Add", "Update", "Delete", "Quit"]
for menu_number, value in enumerate(menu_options, start = 1):
    print (f"{menu_number}. {value}")
    
names = ["Han Solo", "Luke", "Darth Vader", "Yoda", "Leia", "Boba Fett", "Chewbacca"]
bad_names = ("Darth Vader", "Boba Fett")

#Print only the names that are not bad names
for name in names:
    if name not in bad_names:
        print(f"{name} is a good name!")

#Using continue
for name in names:
    if name in bad_names:
        continue #skips to the next element in the list
    print(f"{name} is a good name!")

#break
#Exists a loop
#find the first even number in a list
numbers = [1,9,11,4,8,15,10]

for number in numbers:
    if number % 2==0:
        print (f"The first even number found is {number}")
        break#exit the loop here
print ("Have a groovy day!")

#print the numbers in the list while the sum of the numbers is not over 25
numbers = [5,8,12,20,7,324,234,654,2,34,2,111]
sum = 0
for number in numbers:
    sum += number
    if sum > 25:
        break
    print(number)






