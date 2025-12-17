# topic23.py
# Topic 23 : Encapsulation
# Level : Advanced

TOPIC = {
    "number": 23,
    "title": "Encapsulation",

    "description": [
        "Encapsulation binds data and methods.",
        "Data hiding is achieved.",
        "Private variables use __ prefix.",
        "Public methods access private data.",
        "Improves security.",
        "Controls access to data.",
        "Used in OOP design.",
        "Reduces misuse.",
        "Improves maintainability.",
        "Professional coding practice."
    ],

    "programs": [
        {
            "code": "class A:\n    def __init__(self):\n        self.__x = 10\n    def show(self):\n        print(self.__x)\nobj = A()\nobj.show()",
            "explanation": "Private variable accessed via method."
        },
        {
            "code": "class B:\n    def __init__(self):\n        self._y = 20\nobj = B()\nprint(obj._y)",
            "explanation": "Protected variable example."
        }
    ],

    "mcqs": [
        {"q": "Encapsulation provides?", "options": ["a) Security", "b) Speed"], "ans": "a"},
        {"q": "Private variable prefix?", "options": ["a) __", "b) _"], "ans": "a"},
        {"q": "Data hiding?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Used in OOP?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Improves maintainability?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Access private via?", "options": ["a) Method", "b) Direct"], "ans": "a"},
        {"q": "Controls access?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Reduces misuse?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Public methods?", "options": ["a) Allowed", "b) Not allowed"], "ans": "a"},
        {"q": "Professional practice?", "options": ["a) Yes", "b) No"], "ans": "a"}
    ],

    "practice": [
        "Create private variable.",
        "Access private variable.",
        "Protected variable example.",
        "Explain encapsulation.",
        "Encapsulation advantages.",
        "Encapsulation vs abstraction.",
        "Secure data example.",
        "Getter method.",
        "Setter method.",
        "Real-world example."
    ]
}
