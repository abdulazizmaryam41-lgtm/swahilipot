# Function 1: Get the student's information
def get_student_info(name, age):
    return name, age
    
    # Function 2: Add two numbers
def add_numbers(number1, number2):
    result = number1 + number2 
    return result

name = input("Enter your name: ")
age = int(input("Enter your age: "))
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))


# Function 3: Check the student's age
def check_age(age):
    if age < 18:
        return "You are a minor."
    else:
        return "You are an adult."
    
    # Function 4: Display the result
def display_result(name, age, result):
    print("\n===== Result =====")
    print("Name:", name)
    print("Age:", age)
    print("First number:", number1)
    print("Second number:", number2)
    print("Total:", result)
    print("Status:", check_age(age))

# Get the student's information
name, age = get_student_info(name, age)

# #example numbers
# number1 = 10
# number2 = 5

#Add the two numbers
result = add_numbers(number1, number2)

# Display the result
print("Here are your results:")
display_result(name, age, result)

# Loop to count from 1 to 5
print("\nCounting from 1 to 5:")
for number in range(1, 6):
    print(number)

print("\nThank you for using the program!")
    