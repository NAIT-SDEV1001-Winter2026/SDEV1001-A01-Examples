is_valid = False
play_again = input("Would you like to play again (y/n): ").lower()
while not is_valid:
    play_again = input("MUST BE y/n. Read the rules! Would you like to play again (y/n): ").lower()
    if play_again == "y" or play_again == "n":
        is_valid = True

print("valid")