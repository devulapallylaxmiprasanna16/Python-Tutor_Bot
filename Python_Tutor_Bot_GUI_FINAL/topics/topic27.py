# topic27.py
# Topic 27 : Dictionary Comprehension
# Level : Advanced

TOPIC = {
    "number": 27,
    "title": "Dictionary Comprehension",

    "description": [
        "Dictionary comprehension creates dictionaries concisely.",
        "Uses single-line syntax.",
        "Combines key-value logic.",
        "More readable.",
        "Faster execution.",
        "Supports conditions.",
        "Pythonic style.",
        "Advanced feature.",
        "Used in data processing.",
        "Efficient code."
    ],

    "programs": [
        {
            "code": "sq={x:x*x for x in range(5)}\nprint(sq)",
            "explanation": "Creates dictionary of squares."
        },
        {
            "code": "even={x:x for x in range(10) if x%2==0}\nprint(even)",
            "explanation": "Filters even keys."
        }
    ],

    "mcqs": [
        {"q": "Creates?", "options": ["a) Dict", "b) List"], "ans": "a"},
        {"q": "Single-line?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Faster?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Supports condition?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Pythonic?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Advanced feature?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Readable?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Mapping logic?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Used in data?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Efficient?", "options": ["a) Yes", "b) No"], "ans": "a"}
    ],

    "practice": [
        "Create dict squares.",
        "Filter dictionary.",
        "Convert list to dict.",
        "Use condition.",
        "Explain dict comprehension.",
        "Dict vs loop.",
        "Map values.",
        "Key-value logic.",
        "Nested dict comprehension.",
        "Real-world use."
    ]
}
