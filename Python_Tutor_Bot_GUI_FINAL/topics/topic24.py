# topic24.py
# Topic 24 : Iterators
# Level : Advanced

TOPIC = {
    "number": 24,
    "title": "Iterators",

    "description": [
        "Iterators allow sequential access.",
        "__iter__ returns iterator.",
        "__next__ returns next value.",
        "Used in for loops.",
        "Consumes values one by one.",
        "Raises StopIteration.",
        "Memory efficient.",
        "Custom iterators possible.",
        "Advanced concept.",
        "Used in big data."
    ],

    "programs": [
        {
            "code": "lst = [1,2,3]\nit = iter(lst)\nprint(next(it))",
            "explanation": "Basic iterator example."
        },
        {
            "code": "class Count:\n    def __init__(self, n): self.n=n\n    def __iter__(self): self.i=1; return self\n    def __next__(self):\n        if self.i<=self.n:\n            v=self.i; self.i+=1; return v\n        raise StopIteration\nfor x in Count(3): print(x)",
            "explanation": "Custom iterator example."
        }
    ],

    "mcqs": [
        {"q": "Iterator method?", "options": ["a) __next__", "b) next"], "ans": "a"},
        {"q": "Used in?", "options": ["a) for loop", "b) if"], "ans": "a"},
        {"q": "Memory efficient?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "StopIteration raised when?", "options": ["a) End", "b) Start"], "ans": "a"},
        {"q": "Custom iterator?", "options": ["a) Possible", "b) No"], "ans": "a"},
        {"q": "__iter__ returns?", "options": ["a) Iterator", "b) List"], "ans": "a"},
        {"q": "Consumes values?", "options": ["a) One by one", "b) All"], "ans": "a"},
        {"q": "Advanced concept?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Used in big data?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "Iterator vs iterable?", "options": ["a) Different", "b) Same"], "ans": "a"}
    ],

    "practice": [
        "Create iterator.",
        "Use iter().",
        "Use next().",
        "Custom iterator.",
        "Explain StopIteration.",
        "Iterator vs iterable.",
        "Memory benefit.",
        "Loop with iterator.",
        "Iterator example.",
        "Real-world use."
    ]
}
