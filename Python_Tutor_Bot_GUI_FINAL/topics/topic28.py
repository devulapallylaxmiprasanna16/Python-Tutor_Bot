# topic28.py
# Topic 28 : Decorators
# Level : Advanced

TOPIC = {
    "number": 28,
    "title": "Decorators",

    "description": [
        "Decorators modify function behavior.",
        "Uses @ syntax.",
        "Functions as arguments.",
        "Wrapper functions used.",
        "Reusable logic.",
        "Used in frameworks.",
        "Adds functionality.",
        "Advanced Python concept.",
        "Improves modularity.",
        "Professional usage."
    ],

    "programs": [
        {
            "code": "def deco(f):\n    def wrap():\n        print('Before')\n        f()\n        print('After')\n    return wrap\n@deco\ndef show(): print('Hello')\nshow()",
            "explanation": "Basic decorator example."
        },
        {
            "code": "def upper(f):\n    def wrap(): return f().upper()\n    return wrap\n@upper\ndef msg(): return 'hi'\nprint(msg())",
            "explanation": "Decorator modifying return value."
        }
    ],

    "mcqs": [
        {"q": "Decorator modifies?", "options": ["a) Function", "b) Variable"], "ans": "a"},
        {"q": "@ symbol used for?", "options": ["a) Decorator", "b) Loop"], "ans": "a"},
        {"q": "Wrapper function?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Reusable logic?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Frameworks use?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Advanced?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Function as argument?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Adds behavior?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Improves modularity?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Professional usage?", "options": ["a) Yes", "b) No"], "ans": "a"}
    ],

    "practice": [
        "Create decorator.",
        "Decorator with args.",
        "Timing decorator.",
        "Auth decorator.",
        "Explain decorators.",
        "Decorator vs function.",
        "Multiple decorators.",
        "Return value decorator.",
        "Real-world example.",
        "Decorator advantages."
    ]
}
