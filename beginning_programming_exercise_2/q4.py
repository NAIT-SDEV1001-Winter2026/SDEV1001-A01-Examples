# 4.	Ask the user for
# •	number of pizzas (int)
# •	price per pizza (float, dollars)
# •	tip percent (float; e.g., 15 for 15%)
# •	number of people sharing (int)

# Calculate and print: subtotal, tip amount, total, and amount per person.
# Formatting currency to 2 decimals. Display appropriate inputs and outputs.

#get number of pizzas
pizzas = int(input("How many pizzas? "))
#get price per pizza
price_each = float(input("Price per pizza ($): "))
# get tip
tip_percent = float(input("Tip percent (e.g., 15 for 15%): "))
#get number of people
people = int(input("How many people sharing? "))

#calc subtotal
subtotal = pizzas * price_each
#calc tip
tip = subtotal * (tip_percent / 100)
#calc total
total = subtotal + tip
#calc per person
per_person = total / people

#print results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
print(f"Each person pays: ${per_person:.2f}")

