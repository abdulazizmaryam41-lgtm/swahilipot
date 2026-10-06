def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error:  cannot divide by zero."
    return a / b    

def get_operation():
    print("\nwhat operation do you want?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter 1, 2, 3, or 4: ")
    return choice

keep_going = True

while keep_going:
    # Get numbers from user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Get operstion from user
    operation = get_operation()
    
    # Do the calculation
    if operation == "1":
        result = add(number1, number2)
    elif operation == "2":
        result = subtract(number1, number2)
    elif operation == "3":
        result = multiply(number1, number2)
    elif operation == "4":
        result = divide(number1, number2)
    else:
        result = "Invalid choice"
        
    # show the result
    print("\nResult:", result)
    
    # Ask if they want to continue
    again = input("\nDo you want to do another calculation? (yes or no): ")
    if again.lower() != "yes":
        keep_going = False
        
    print("Thank you for using the calculate!")
    