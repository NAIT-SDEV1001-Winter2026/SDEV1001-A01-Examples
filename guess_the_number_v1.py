#Same but add the ability to play again if the user wants to.

import random
play_again = "y"

while play_again =="y":
#Generate a random number between 1 and 100
    random_number = random.randint(1,100)
    guesses = 0
    is_done = False

    while not is_done:#run at least once
    #get guess from user
        guess = int (input("Enter a number (1-100): "))
    #Add 1 to guesses
        guesses += 1
    #Determine if it is correct, too high, too low. Print message
        if guess == random_number:
            print("You win!")
            is_done = True
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")
    #If correct display how many guesses it took
    print(f"It to you {guesses} guesses")
#Ask to play again
    is_valid = False
    while not is_valid:
        play_again = input("Would you like to play again (y): ").lower()
        if input == "y" or input == "n":
            is_valid = True

