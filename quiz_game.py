# simple Quiz game 
# This program asks the user questions and calculates their score

# Funcion 1: Get the user's name
def get_name():
    name = input("What is your name? ")
    return name 


# Function 2: Ask a question and check the answer
def ask_question(question, correct_answer):
    answer = input(question + " ")

  # Use an if statement to check the user's answer 
    if answer.lower() == correct_answer.lower():
     print("Correct!")
     return True
    else:
     print("wrong!")
     return False
    
    
    # Function 3: Display the final score
def show_result(name, score, total):
        print("\n---Final Result---")
        print("player:", name)
        print("score:", score, "out of", total)
        
        
# Make a decision based on the score
        if score == total:
         print("Excellent! You got everything correct!")
        elif score >= 2:
         print("Good job!")
        else:
         print("Keep practicing!")
    
    
# Main part of the program
name = get_name()

# A list is a data type that stores multiple values
questions = [
    ("what is 2 + 2?", "4"),
    ("what is the capital of Kenya?", "Nairobi"),
    ("what is the largest ocean?", "Pacific"),
    
]


# An integer is used to keep track of the score
score = 0

# A loop repeats the code for every question
for question, correct_answer in questions:
    
    # Call the ask_question function
    if ask_question(question, correct_answer):
        score += 1
        
# Show the final result
show_result(name, score, len(questions))
    
    
    
        