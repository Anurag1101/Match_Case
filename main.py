# example of match case in python similar to switch case in C++ and Java

try: 
    x = int(input("Enter a number between 1 and 7: "))
    
    match x:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Error: Please enter a number between 1 and 7.")
            
except ValueError:  # error handling
    print("Error: Invalid input. Please enter an integer.")