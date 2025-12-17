# topic25.py
# Topic 25 : Generators
# Level : Advanced

TOPIC = {
    "number": 25,
    "title": "Generators",

    "description": [
        "Generators produce values lazily.",
        "Use yield keyword.",
        "Memory efficient.",
        "Alternative to iterators.",
        "Values generated one at a time.",
        "Stops automatically.",
        "Used for large data.",
        "Simpler than iterators.",
        "Advanced Python feature.",
        "High performance."
    ],

    "programs": [
        {
            "code": "def gen():\n    yield 1\n    yield 2\nfor x in gen(): print(x)",
            "explanation": "Basic generator example."
        },
        {
            "code": "def squares(n):\n    for i in range(n):\n        yield i*i\nprint(list(squares(4)))",
            "explanation": "Generates squares."
        }
    ],

    "mcqs": [
        {"q": "Keyword used?", "options": ["a) yield", "b) return"], "ans": "a"},
        {"q": "Memory efficient?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Values generated?", "options": ["a) One by one", "b) All"], "ans": "a"},
        {"q": "Used for?", "options": ["a) Large data", "b) Small"], "ans": "a"},
        {"q": "Alternative to?", "options": ["a) Iterator", "b) Loop"], "ans": "a"},
        {"q": "Simpler than iterator?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Stops automatically?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Advanced feature?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Performance?", "options": ["a) High", "b) Low"], "ans": "a"},
        {"q": "Generator returns?", "options": ["a) Iterator", "b) List"], "ans": "a"}
    ],

    "practice": [
        "Create generator.",
        "Use yield.",
        "Generate numbers.",
        "Generate squares.",
        "Generator vs list.",
        "Memory usage test.",
        "Fibonacci generator.",
        "Even number generator.",
        "Explain generators.",
        "Real-world usage."
    ]
}
