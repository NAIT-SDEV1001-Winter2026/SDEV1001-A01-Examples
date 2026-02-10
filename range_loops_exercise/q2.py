rows = int (input("Enter the number of rows: "))

for row in range(1,rows + 1):
    spaces = rows - row# spaces before the star(s)
    stars = 2 * row -1 # number of stars

    print (" " * spaces + "*" * stars ) 
