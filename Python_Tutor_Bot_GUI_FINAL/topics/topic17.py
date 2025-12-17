# topic17.py
# Topic 17 : Exception Handling
# Level : Intermediate

TOPIC = {
    "number": 17,
    "title": "Exception Handling",

    "description": [
        "Exception handling handles runtime errors.",
        "try block contains risky code.",
        "except block handles error.",
        "else runs when no error.",
        "finally always executes.",
        "Prevents program crash.",
        "Improves user experience.",
        "Handles invalid input.",
        "Used in real programs.",
        "Important safety feature."
    ],

    "programs": [
        {
            "code": "try:\n    a = int(input())\n    print(10/a)\nexcept:\n    print('Error occurred')",
            "explanation": "Handles division error."
        },
        {
            "code": "try:\n    print(x)\nexcept NameError:\n    print('Variable not defined')",
            "explanation": "Handles NameError."
        }
    ],

    "mcqs": [
        {"q": "Block for risky code?", "options": ["a) try", "b) except"], "ans": "a"},
        {"q": "Handles error?", "options": ["a) except", "b) finally"], "ans": "a"},
        {"q": "Runs always?", "options": ["a) finally", "b) else"], "ans": "a"},
        {"q": "Avoids crash?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Handles runtime errors?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "NameError handled by?", "options": ["a) except", "b) try"], "ans": "a"},
        {"q": "else runs when?", "options": ["a) No error", "b) Error"], "ans": "a"},
        {"q": "finally runs?", "options": ["a) Always", "b) Sometimes"], "ans": "a"},
        {"q": "Used for?", "options": ["a) Safety", "b) Speed"], "ans": "a"},
        {"q": "Exception handling improves?", "options": ["a) UX", "b) Memory"], "ans": "a"}
    ],

    "practice": [
        "Handle ZeroDivisionError.",
        "Handle ValueError.",
        "Use else block.",
        "Use finally block.",
        "Multiple except blocks.",
        "Custom message.",
        "Input validation.",
        "Explain try-except.",
        "Handle file error.",
        "Why exceptions needed?"
    ]
}
