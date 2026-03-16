students = {}

# Create 3 students
for i in range(3):
    name = input("Enter student name: ")
    #For each student create 3 grades
    grades = []
    for j in range(3):
        grade = int(input(f"Enter grade {j+1}: "))
        grades.append(grade)
    #Add the new student(keys and values)
    students[name] = {
        "grades": grades,
        "average": 0
    }

# Calculate averages
#For each student, retrieve the grades list and calculate the everage of all the grades in the grades list
for student in students:#for each student
    grades = students[student]["grades"]#list of grades for that student
    students[student]["average"] = sum(grades) / len(grades)#set the average for that student

print("\nStudent Report")
#For each student and info(grades and average)
for student, info in students.items():
    print(f"\n{student}")#Print the name
    print(f"Grades: {info["grades"]}")#Print the grades list
    print(f"Average: {round(info["average"], 2)}")#Print the average
    #loop through all the grades, if the grade is over 80, add the grade to the high_grades list
    high_grades = [g for g in info["grades"] if g > 80]
    print(f"High Grades: {high_grades} ")

