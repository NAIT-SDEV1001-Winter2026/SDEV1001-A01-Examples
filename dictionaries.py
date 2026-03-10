#Store data in key-value pairs (like **kwargs)
#keys are unique and usually strings; values can be any datatype
#Good for representing structered data like a product
#the value can be another dictionary, list, tuple

#Student 
student = {"name": "Homer", "age": 42, "email": "Homer@gmail.com"}
#Create a dictionary in a car variable with make, model, year keys/values
car = {"make": "Jeep", "model":"TJ", "year":1999}

#accessing values
print(student["name"])
student["age"] = 52

#Create a new entry
student["grade"] = 95

#accessing non existing key is an error
# print(student["favorite_number"]) #KeyError

#this error can be avoided with get()
print(student.get("abc","N/A"))#If there is no abc key

#checking if key exists
if "email" in student:#is this key in the student dictionary
    print(f"Email is: {student["email"]}")
else:
    print("No email")

#Values can be other dictionaries, lists, tuples as well
inventory ={
            "apple": {"price": .50, "stock": 40},
            "pear": {"price": .80, "stock": 30} 
}

#Accessing nested values
print(f"Item:Price: {inventory["apple"]["price"]:.2f} Stock: {inventory["apple"]["stock"]} ") 

#Looping 
#loop through a dictionary (keys and values)
for key in student:#loop through the keys. Could use student.keys()
    print(f"{key}: {student[key]}")#access each value by the key

grades = {"Bart": 40, "Homer": 20, "Lisa": 90}
#OR
for name,grade in grades.items():
    print(f"{name}: {grade}")



grades = {"Bart": 40, "Homer": 20, "Lisa": 90}
#Print all the names of the students in the grades dictionary
for name in grades:#loop through the keys. Could use student.keys()
    print(f"{name}")

#print all the grades
print ("Grades:")
for grade in grades.values():
    print(grade)

#use the grades dictionary, calculate and display the average grade
sum = 0
for grade in grades.values():
    sum += grade
answer = sum / len(grades)
print(f"Average grade: {answer}")

#Exercise
inventory = {"apples": 0, "bananas": 0, "oranges": 0}
delivery = ["apples", "bananas", "apples", "oranges", "apples"]
#use the delivery list to update the stock quantities in the inventory dictionary

for item in delivery:
    inventory[item] +=1#increase the count for that item in the dictionary

for fruit, count in inventory.items():
    print(f"{fruit}: {count}")
