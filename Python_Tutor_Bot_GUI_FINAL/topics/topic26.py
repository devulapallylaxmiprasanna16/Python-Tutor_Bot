# topic26.py
# Topic 26 : List Comprehension
# Level : Advanced

TOPIC = {
    "number": 26,
    "title": "List Comprehension",

    "description": [
        "List comprehension creates lists concisely.",
        "Uses single-line syntax.",
        "Combines loop and condition.",
        "More readable code.",
        "Faster than loops.",
        "Supports filtering.",
        "Supports mapping.",
        "Advanced Python feature.",
        "Used widely.",
        "Pythonic style."
    ],

    "programs": [
        {
            "code": "nums=[1,2,3]\nsq=[x*x for x in nums]\nprint(sq)",
            "explanation": "Squares using list comprehension."
        },
        {
            "code": "even=[x for x in range(10) if x%2==0]\nprint(even)",
            "explanation": "Filters even numbers."
        }
    ],

    "mcqs": [
        {"q": "Creates?", "options": ["a) List", "b) Tuple"], "ans": "a"},
        {"q": "One-line syntax?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Faster?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Supports filter?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Pythonic?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Combines?", "options": ["a) Loop + condition", "b) Only loop"], "ans": "a"},
        {"q": "Readable?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Advanced?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Mapping supported?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Used widely?", "options": ["a) Yes", "b) No"], "ans": "a"}
    ],

    "practice": [
        "Square list.",
        "Filter even numbers.",
        "Create list 1–10.",
        "Odd numbers list.",
        "Double values.",
        "List comprehension vs loop.",
        "Nested list comprehension.",
        "Convert string to list.",
        "Condition inside list.",
        "Explain list comprehension."
    ]
}
