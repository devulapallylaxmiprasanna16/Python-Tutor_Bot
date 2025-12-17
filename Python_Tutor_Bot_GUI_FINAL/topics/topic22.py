# topic22.py
# Topic 22 : Polymorphism
# Level : Advanced

TOPIC = {
    "number": 22,
    "title": "Polymorphism",

    "description": [
        "Polymorphism means many forms.",
        "Same method name with different behavior.",
        "Method overriding implements polymorphism.",
        "Method overloading simulated in Python.",
        "Operator overloading possible.",
        "Dynamic binding supported.",
        "Enhances flexibility.",
        "Improves scalability.",
        "OOP core principle.",
        "Used in frameworks."
    ],

    "programs": [
        {
            "code": "class A:\n    def show(self):\n        print('A')\nclass B(A):\n    def show(self):\n        print('B')\nobj = B()\nobj.show()",
            "explanation": "Runtime polymorphism using overriding."
        },
        {
            "code": "print(len('Python'))\nprint(len([1,2,3]))",
            "explanation": "Same function behaves differently."
        }
    ],

    "mcqs": [
        {"q": "Polymorphism means?", "options": ["a) Many forms", "b) One form"], "ans": "a"},
        {"q": "Implemented by?", "options": ["a) Overriding", "b) Loop"], "ans": "a"},
        {"q": "Same method name?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Dynamic binding?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Operator overloading?", "options": ["a) Possible", "b) Impossible"], "ans": "a"},
        {"q": "Improves flexibility?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Frameworks use?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Compile-time polymorphism?", "options": ["a) Limited", "b) Full"], "ans": "a"},
        {"q": "OOP principle?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Method behavior differs?", "options": ["a) Yes", "b) No"], "ans": "a"}
    ],

    "practice": [
        "Override method.",
        "Demonstrate polymorphism.",
        "len() examples.",
        "Create base and child.",
        "Explain polymorphism.",
        "Operator overloading example.",
        "Runtime polymorphism.",
        "Advantages of polymorphism.",
        "Real-world example.",
        "Polymorphism vs inheritance."
    ]
}
