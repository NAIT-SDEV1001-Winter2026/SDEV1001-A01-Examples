# 3.	A bag of cookies holds 40 cookies. The calorie information on the bag claims that there are 10 "servings" in the bag and that a serving equals 300 calories. Write a program that asks the user to input how many cookies they ate and then reports how many total calories were consumed.

# Output:
# How many cookies did you eat? 25
# You ate 25 cookies
# Which is equal to: 1875.0 calories

COOKIES_PER_BAG = 40
SERVINGS_PER_BAG = 10
CALORIES_PER_SERVING = 300

#get number of cookies
cookies = int(input("How many cookies did you eat? "))
#calculate calories consumed
calories_consumed = (cookies/COOKIES_PER_BAG) * (SERVINGS_PER_BAG * CALORIES_PER_SERVING)
#print how many cookies
print (f"You ate {cookies} cookies")
# print calories 
print (f"Which is equal to {calories_consumed} calories")


 
