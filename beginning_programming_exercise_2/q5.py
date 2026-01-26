# 5.	Ask the user for a currency amount and display the number of dollars, quarters, dimes, nickels, and pennies in that amount. Display appropriate inputs and outputs.

#get amount
amount = float(input("Enter a dollar amount (e.g. 3.87): "))
#convert amount to pennies
cents = int(amount * 100)

#calculate dollars
#divide by 100 and round down (floor division)
dollars = cents // 100
#calcuate remainder
#remainder = cents modulous 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

print("Coin Breakdown:")
print("Dollars:", dollars)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)



 
 

 