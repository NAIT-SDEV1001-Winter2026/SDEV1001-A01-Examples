def get_and_calculate_average (sum,count):
    average = sum/count
    return average

def get_valid_positive_float(prompt):
    while True:
            user_input = input(prompt)
            try:
                user_input = float(user_input)
                if user_input > 0:                                                        
                    break
                else: 
                    print("Please enter a positive number.\n")
            except ValueError:
                print("That wasn't a valid number. Please try again.\n")
    return user_input 

def get_valid_positive_int(prompt):
    while True:       
        user_input = input(prompt)
        try:           
            user_input = int(user_input) 
            if user_input > 0:            
                break
            else:
                print("Please enter an integer greater than 0.\n")           
        except ValueError:
            print("That wasn't a valid integer. Please try again.\n")
    return user_input