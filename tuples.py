#Same as a list but immutable (Cannot change)
#Defined with () instead of []

winter_months = ("December", "January", "February")

#Ask the user for a month name
#if it is a winter month, print "Winter", othewise print("Not winter")

user_month = input("Enter a month: ")

if user_month in winter_months:
    print("Winter")
else:
    print("Not Winter")
