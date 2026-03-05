import random
#Randomly generate a coin toss value
def get_coin_flip():     
    toss = random.choice(["heads", "tails"])
    return toss
#Get a valid guess from the user
def get_valid_user_guess():     
    while True:
        user_guess = input("Guess the coin flip! Enter heads or tails (Heads/Tails): ").lower()
        if user_guess == "heads" or user_guess == "tails":            
                break
        else:
            print("You must enter Heads or Tails!")
    return user_guess

#Display if they are correct or not
def display_result(toss,user_guess):     
    if toss == user_guess:
        print("you guessed correct!")    
    else:
        print("you guessed wrong!")

toss = get_coin_flip()
user_guess = get_valid_user_guess()
display_result(toss,user_guess)