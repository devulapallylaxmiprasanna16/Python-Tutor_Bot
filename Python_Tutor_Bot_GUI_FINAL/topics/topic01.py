# topic01.py
# ===============================
# Topic 01 : VARIABLES
# Level : Beginner
# ===============================

TOPIC = {
    "number": 1,
    "title": "Variables",

    # -------- DESCRIPTION (10 lines) --------
    "description": [
        "Variables are used to store data values in memory.",
        "Python variables do not need explicit declaration.",
        "They are dynamically typed, meaning type can change.",
        "The assignment operator '=' is used to assign values.",
        "Variable names should be meaningful and readable.",
        "Python variable names are case-sensitive.",
        "Variables can store numbers, strings, and objects.",
        "Values stored in variables can be modified.",
        "Variables help reuse and manage data easily.",
        "They form the foundation of every Python program."
    ],

    # -------- SAMPLE PROGRAMS (2) --------
    "programs": [
        {
            "code": 
"""a = 10
b = 20
sum = a + b
print("Sum:", sum)""",
            "explanation": 
            "This program stores two numbers in variables and adds them using the + operator."
        },
        {
            "code": 
"""name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Name:", name)
print("Age:", age)""",
            "explanation": 
            "This program takes user input, stores values in variables, and prints them."
        }
    ],

    # -------- MCQs (10 QUESTIONS) --------
    "mcqs": [
        {
            "q": "Which symbol is used to assign a value to a variable?",
            "options": ["a) =", "b) ==", "c) :"],
            "ans": "a"
        },
        {
            "q": "Python variables are ___ typed.",
            "options": ["a) Statically", "b) Dynamically", "c) Manually"],
            "ans": "b"
        },
        {
            "q": "Which of the following is a valid variable name?",
            "options": ["a) 1value", "b) value_1", "c) value-1"],
            "ans": "b"
        },
        {
            "q": "Python variable names are case-sensitive?",
            "options": ["a) Yes", "b) No"],
            "ans": "a"
        },
        {
            "q": "Which operator assigns a value?",
            "options": ["a) +", "b) =", "c) =="],
            "ans": "b"
        },
        {
            "q": "What type of data can variables store?",
            "options": ["a) Only numbers", "b) Only strings", "c) Any data type"],
            "ans": "c"
        },
        {
            "q": "Can a variable value be changed after assignment?",
            "options": ["a) Yes", "b) No"],
            "ans": "a"
        },
        {
            "q": "Which keyword is used to declare variables in Python?",
            "options": ["a) var", "b) int", "c) No keyword needed"],
            "ans": "c"
        },
        {
            "q": "What will x = 5; x = 10 do?",
            "options": ["a) Error", "b) Change value", "c) Create two variables"],
            "ans": "b"
        },
        {
            "q": "Variables mainly help in?",
            "options": ["a) Storing data", "b) Printing only", "c) Looping only"],
            "ans": "a"
        }
    ],

    # -------- PRACTICE QUESTIONS (10) --------
    "practice": [
        "Write a program to store and print your name.",
        "Write a program to swap two variables.",
        "Store two numbers and print their sum.",
        "Store a float value and print its type.",
        "Change a variable value and print it.",
        "Take user age and display it.",
        "Store a string and an integer in variables.",
        "Assign multiple variables in one line.",
        "Write rules for naming variables.",
        "Explain why variables are important."
    ]
}
