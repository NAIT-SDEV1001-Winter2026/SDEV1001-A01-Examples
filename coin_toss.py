#NO FUNCTIONS
#Randomly generate a coin toss value
#Get a valid guess from the user
#Display if they are correct or not
import random
#Randomly generate a coin toss value
toss = random.choice(["heads", "tails"])
#Get a valid guess from the user
while True:
    user_guess = input("Guess the coin flip! Enter heads or tails (Heads/Tails): ").lower()
    if user_guess == "heads" or user_guess == "tails":            
            break
    else:
        print("You must enter Heads or Tails!")
#Display if they are correct or not
if toss == user_guess:
    print("you guessed correct!")    
else:
    print("you guessed wrong!")

