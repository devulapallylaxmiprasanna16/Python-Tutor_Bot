# topic20.py
# Topic 20 : Constructors
# Level : Intermediate

TOPIC = {
    "number": 20,
    "title": "Constructors",

    "description": [
        "Constructor initializes object data.",
        "__init__ is constructor method.",
        "Called automatically when object created.",
        "Used to assign values.",
        "Belongs to class.",
        "Can accept parameters.",
        "Improves object setup.",
        "Used in OOP.",
        "Very important concept.",
        "Professional usage."
    ],

    "programs": [
        {
            "code": "class A:\n    def __init__(self):\n        print('Constructor called')\nobj = A()",
            "explanation": "Demonstrates default constructor."
        },
        {
            "code": "class Student:\n    def __init__(self,name):\n        self.name = name\ns = Student('Ram')\nprint(s.name)",
            "explanation": "Parameterized constructor example."
        }
    ],

    "mcqs": [
        {"q": "Constructor name?", "options": ["a) __init__", "b) init"], "ans": "a"},
        {"q": "Called when?", "options": ["a) Object created", "b) Class defined"], "ans": "a"},
        {"q": "Belongs to?", "options": ["a) Class", "b) Object"], "ans": "a"},
        {"q": "Assign values?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Accept parameters?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Runs automatically?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Used in?", "options": ["a) OOP", "b) Loop"], "ans": "a"},
        {"q": "Multiple constructors?", "options": ["a) No", "b) Yes"], "ans": "a"},
        {"q": "self refers to?", "options": ["a) Object", "b) Class"], "ans": "a"},
        {"q": "Constructor improves?", "options": ["a) Initialization", "b) Speed"], "ans": "a"}
    ],

    "practice": [
        "Create default constructor.",
        "Create parameterized constructor.",
        "Initialize object data.",
        "Use self keyword.",
        "Create multiple objects.",
        "Explain constructor.",
        "Constructor vs method.",
        "Real-world example.",
        "OOP with constructor.",
        "Advantages of constructor."
    ]
}
