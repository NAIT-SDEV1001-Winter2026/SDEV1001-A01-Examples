days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_of_weekend = ("Saturday", "Sunday")

for day_number, day in enumerate(days_of_week, start = 1):
    print (f"{day} is day number {day_number} of the week")
    if day in days_of_weekend:
        print (f"s{day} is a weekend day")    
    else:
        print (f"{day} is a weekday")    