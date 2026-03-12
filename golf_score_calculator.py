def calculate_average(*scores):
    sum = 0
    for value in scores:
        sum += value
    average = sum/(len(scores))
    return average

print("Golf Score Calculator")

sum = 0
scores = []
top_5_sum = 0

while True:
    #get scores from the user
    score = input("Enter another score: (q to quit and calculate): ")
    #if q then quit the loop
    if score == "q":
        break            
    scores.append(int(score))

#calculate average
average = calculate_average(*scores)    
#display average
print(f"Your average golf score is {average}")

#is there 5 scores to calculate handicap?
if len(scores) < 5:
    print("Your handicap is: Need at least 5 scores to calculate a handicap")
else:    
#Sort the list ascending
    scores.sort()

    #Calculate the sum of the first 5 scores in the list and put in a variable
    for score in scores[0:5]:
        top_5_sum += score

    #calculate the average of the first 5 scores and subtract 72
    handicap = top_5_sum/5 - 72

    #print handicap
    print(f"Your handicap is: {handicap:.2f}")


