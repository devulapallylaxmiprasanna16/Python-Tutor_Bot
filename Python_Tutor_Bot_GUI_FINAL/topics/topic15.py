# topic15.py
# Topic 15 : Lambda Functions
# Level : Intermediate

TOPIC = {
    "number": 15,
    "title": "Lambda Functions",

    "description": [
        "Lambda functions are anonymous functions.",
        "Defined using lambda keyword.",
        "Single expression only.",
        "Shorter syntax.",
        "Can take multiple arguments.",
        "Returns value automatically.",
        "Used with map().",
        "Used with filter().",
        "Used with reduce().",
        "Advanced feature."
    ],

    "programs": [
        {
            "code": "add = lambda a,b: a+b\nprint(add(3,4))",
            "explanation": "Adds two numbers using lambda."
        },
        {
            "code": "nums = [1,2,3,4]\neven = list(filter(lambda x:x%2==0, nums))\nprint(even)",
            "explanation": "Filters even numbers using lambda."
        }
    ],

    "mcqs": [
        {"q": "Lambda is?", "options": ["a) Anonymous", "b) Named"], "ans": "a"},
        {"q": "Lambda keyword?", "options": ["a) lambda", "b) def"], "ans": "a"},
        {"q": "Lambda can have?", "options": ["a) One expression", "b) Many statements"], "ans": "a"},
        {"q": "Returns value?", "options": ["a) Automatically", "b) return"], "ans": "a"},
        {"q": "Used with map?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Used with filter?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Lambda readability?", "options": ["a) Less", "b) More"], "ans": "a"},
        {"q": "Multiple arguments?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Lambda block size?", "options": ["a) One line", "b) Multi-line"], "ans": "a"},
        {"q": "Advanced feature?", "options": ["a) Yes", "b) No"], "ans": "a"}
    ],

    "practice": [
        "Add two numbers lambda.",
        "Square number lambda.",
        "Find max lambda.",
        "Even filter lambda.",
        "Odd filter lambda.",
        "Map square lambda.",
        "Lambda with list.",
        "Lambda with tuple.",
        "Explain lambda.",
        "Lambda vs function."
    ]
}
