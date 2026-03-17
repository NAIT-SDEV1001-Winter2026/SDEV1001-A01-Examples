#Basic tasks in working with a file:
    #Open the file
    #Work with the file
    #Close the file

#Write to a file in the same folder as the py file

from pathlib import Path#Importing the Path class

#Set the path to your text file to be the same folder as the py file (this folder)
base_dir = Path(__file__).parent#What is the path of the folder the file is in. Where are we?
file_path = base_dir/"movies.txt"#path to the text file we will create/use

#with will open the file, "a" will allow us to append to the file and close it when done
#when appending to a file, if it does not exist, the file will be created
#f is an alias to the file
with open(file_path,"a") as f:
    f.write("Dune\n")
    f.write("GhostBusters!\n")

#Change "a" to "w"
#w means overwrite everything on the file
with open(file_path,"w") as f:
    f.write("Lord of the rings\n")
    f.write("Star Trek!\n")
    f.write("Annie\n")
    
#Exercise:
#Using a new file called food.py write to a text file called food_items.txt
#In a loop, ask the user for a food_item and add it to the current text file. Keep looping until the user enters "olives"
#Add the items to what is already on the list

#Reading from a file
#Use the mode "r"
#Read all the lines from the file into a list
try:
    with open(file_path,"r") as f:
        new_list = f.readlines()#reads all the lines from the file into a list
except FileNotFoundError:
    print("File not found")

print(new_list)

#loop through list
for item in new_list:
    print(item.strip())#remove the \n from the row

#Functions for basic file IO
#Read a file into a list and return the list
def read_file(file_name):    
    with open(file_name, "r") as f:
        new_list = f.readlines()
    return new_list    
   
test_list = read_file(file_path)
print(test_list)

def add_to_file(file_name,text):
    with open (file_name,"a") as f:
        f.write(f"{text}\n")

def write_file(file_name,text):
    with open (file_name,"w") as f:
        f.write(f"{text}\n")

