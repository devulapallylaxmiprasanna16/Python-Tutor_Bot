# topic21.py
# Topic 21 : Inheritance
# Level : Advanced

TOPIC = {
    "number": 21,
    "title": "Inheritance",

    "description": [
        "Inheritance allows one class to acquire another class properties.",
        "Parent class is also called base class.",
        "Child class is also called derived class.",
        "Inheritance promotes code reusability.",
        "Single inheritance has one parent.",
        "Multiple inheritance has multiple parents.",
        "Method overriding is possible.",
        "super() accesses parent methods.",
        "Improves maintainability.",
        "Core OOP concept."
    ],

    "programs": [
        {
            "code": "class A:\n    def show(self):\n        print('Parent')\nclass B(A):\n    pass\nobj = B()\nobj.show()",
            "explanation": "Child class inherits parent method."
        },
        {
            "code": "class A:\n    def show(self):\n        print('A')\nclass B(A):\n    def show(self):\n        print('B')\nobj = B()\nobj.show()",
            "explanation": "Method overriding example."
        }
    ],

    "mcqs": [
        {"q": "Inheritance provides?", "options": ["a) Code reuse", "b) Speed"], "ans": "a"},
        {"q": "Parent class also called?", "options": ["a) Base", "b) Child"], "ans": "a"},
        {"q": "Child class also called?", "options": ["a) Derived", "b) Parent"], "ans": "a"},
        {"q": "super() used for?", "options": ["a) Parent access", "b) Loop"], "ans": "a"},
        {"q": "Multiple parents?", "options": ["a) Multiple inheritance", "b) Single"], "ans": "a"},
        {"q": "Override means?", "options": ["a) Redefine", "b) Delete"], "ans": "a"},
        {"q": "Improves maintainability?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "OOP concept?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Child gets parent methods?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Inheritance reduces?", "options": ["a) Duplication", "b) Logic"], "ans": "a"}
    ],

    "practice": [
        "Create parent and child class.",
        "Demonstrate single inheritance.",
        "Demonstrate method overriding.",
        "Use super().",
        "Multiple inheritance example.",
        "Explain inheritance.",
        "Advantages of inheritance.",
        "Disadvantages of inheritance.",
        "Real-world example.",
        "Inheritance vs composition."
    ]
}
