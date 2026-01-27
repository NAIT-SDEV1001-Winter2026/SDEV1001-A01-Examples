#prompt the user for a movie name 
movie_name = input("Enter a movie name: ")
#if "star wars" print 2 prints
if movie_name.upper() == "STAR WARS":
    print("Incredible movie!")
    print("Check it out!")
    #if "Star Trek" print 1 print
elif movie_name.upper() == "STAR TREK":
    print ("Great Movie!")
#If "Maz Runner"  print 1 print
elif movie_name.upper() == "Maze Runner":
    print("Cool!")
else:
    print("Unknown Movie!")#otherwise print "Unknown movie"

#Match Version

match movie_name.upper():
    case "STAR WARS":
         print("Incredible movie!")
         print("Check it out!")
    case "STAR TREK":
        print ("Great Movie")
    case "MAZE RUNNER":
        print ("Cool")
    case _:
        print("Unknown Movie")
    


