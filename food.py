#Exercise:
#Using a new file called food.py write to a text file called food_items.txt
#In a loop, ask the user for a food_item and add it to the current text file. Keep looping until the user enters "olives"
#Add the items to what is already on the list

from pathlib import Path

base_dir = Path(__file__).parent
file_path = base_dir/"food_items.txt"

with open(file_path,"a") as f:
    while True:
        user_input = input("Enter a food item: ")
        if user_input.lower() =="olives":
            break
        f.write(f"{user_input}\n") 
