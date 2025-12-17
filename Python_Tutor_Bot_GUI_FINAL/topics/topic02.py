# topic02.py
# Topic 02 : Data Types
# Level : Beginner

TOPIC = {
    "number": 2,
    "title": "Data Types",

    "description": [
        "Data types define the type of data stored in variables.",
        "Python supports integer, float, and string types.",
        "Collection data types include list, tuple, set, and dictionary.",
        "Python is dynamically typed.",
        "The type() function checks data type.",
        "Some data types are mutable.",
        "Some data types are immutable.",
        "Correct data type avoids errors.",
        "Data types help memory management.",
        "They are a core Python concept."
    ],

    "programs": [
        {
            "code": "a = 10\nb = 3.5\nc = 'Python'\nprint(type(a), type(b), type(c))",
            "explanation": "Shows different data types using type() function."
        },
        {
            "code": "x = [1, 2, 3]\ny = (1, 2, 3)\nprint(type(x), type(y))",
            "explanation": "Demonstrates list and tuple data types."
        }
    ],

    "mcqs": [
        {"q": "Which function checks data type?", "options": ["a) check()", "b) type()", "c) data()"], "ans": "b"},
        {"q": "Which is immutable?", "options": ["a) List", "b) Tuple", "c) Set"], "ans": "b"},
        {"q": "Python is ___ typed.", "options": ["a) Static", "b) Dynamic"], "ans": "b"},
        {"q": "Which stores key-value pairs?", "options": ["a) List", "b) Tuple", "c) Dictionary"], "ans": "c"},
        {"q": "Which is mutable?", "options": ["a) Tuple", "b) List"], "ans": "b"},
        {"q": "String is enclosed in?", "options": ["a) Quotes", "b) Brackets"], "ans": "a"},
        {"q": "Which stores unique values?", "options": ["a) List", "b) Set"], "ans": "b"},
        {"q": "Float stores?", "options": ["a) Whole numbers", "b) Decimal values"], "ans": "b"},
        {"q": "type(10) returns?", "options": ["a) int", "b) number"], "ans": "a"},
        {"q": "Which is collection type?", "options": ["a) int", "b) list"], "ans": "b"}
    ],

    "practice": [
        "Check data type of a number.",
        "Create list and tuple.",
        "Find mutable data types.",
        "Convert int to float.",
        "Convert string to int.",
        "Print type of user input.",
        "Create dictionary.",
        "Explain mutable vs immutable.",
        "Create set with values.",
        "Write data type examples."
    ]
}
