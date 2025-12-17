# topic03.py
# Topic 03 : Input and Output
# Level : Beginner

TOPIC = {
    "number": 3,
    "title": "Input and Output",

    "description": [
        "input() is used to take input from user.",
        "print() is used to display output.",
        "Input is always string by default.",
        "Type casting is required for numbers.",
        "Multiple values can be printed.",
        "Formatted output is supported.",
        "User interaction is possible.",
        "print() supports separators.",
        "print() supports end parameter.",
        "Essential for user programs."
    ],

    "programs": [
        {
            "code": "name = input('Enter name: ')\nprint('Hello', name)",
            "explanation": "Takes user input and prints greeting."
        },
        {
            "code": "a = int(input())\nb = int(input())\nprint(a + b)",
            "explanation": "Adds two numbers taken from user."
        }
    ],

    "mcqs": [
        {"q": "input() returns?", "options": ["a) int", "b) string"], "ans": "b"},
        {"q": "print() is used for?", "options": ["a) input", "b) output"], "ans": "b"},
        {"q": "Type casting is used for?", "options": ["a) conversion", "b) printing"], "ans": "a"},
        {"q": "Which displays output?", "options": ["a) input()", "b) print()"], "ans": "b"},
        {"q": "Default input type?", "options": ["a) string", "b) int"], "ans": "a"},
        {"q": "print supports?", "options": ["a) sep", "b) end"], "ans": "a"},
        {"q": "input is interactive?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Multiple print allowed?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "print('a','b') prints?", "options": ["a) ab", "b) a b"], "ans": "b"},
        {"q": "input used in?", "options": ["a) User programs", "b) OS only"], "ans": "a"}
    ],

    "practice": [
        "Take name and age.",
        "Add two numbers.",
        "Multiply user inputs.",
        "Print formatted output.",
        "Take float input.",
        "Display message.",
        "Print multiple values.",
        "Use sep parameter.",
        "Use end parameter.",
        "Explain input vs print."
    ]
}
