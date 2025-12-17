# topic06.py
# Topic 06 : Loops
# Level : Beginner

TOPIC = {
    "number": 6,
    "title": "Loops",

    "description": [
        "Loops repeat a block of code.",
        "for loop iterates sequence.",
        "while loop runs on condition.",
        "range() generates numbers.",
        "break stops loop.",
        "continue skips iteration.",
        "Nested loops allowed.",
        "Reduces code repetition.",
        "Used in data processing.",
        "Core Python concept."
    ],

    "programs": [
        {
            "code": "for i in range(5):\n    print(i)",
            "explanation": "Prints numbers using for loop."
        },
        {
            "code": "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1",
            "explanation": "Prints numbers using while loop."
        }
    ],

    "mcqs": [
        {"q": "Which loop uses range?", "options": ["a) for", "b) while"], "ans": "a"},
        {"q": "Which loop checks condition?", "options": ["a) while", "b) for"], "ans": "a"},
        {"q": "break does?", "options": ["a) stop loop", "b) skip"], "ans": "a"},
        {"q": "continue does?", "options": ["a) stop", "b) skip"], "ans": "b"},
        {"q": "Nested loop means?", "options": ["a) loop inside loop", "b) condition"], "ans": "a"},
        {"q": "range generates?", "options": ["a) numbers", "b) strings"], "ans": "a"},
        {"q": "Loop repeats?", "options": ["a) code", "b) comment"], "ans": "a"},
        {"q": "while ends when?", "options": ["a) condition false", "b) true"], "ans": "a"},
        {"q": "for loop used for?", "options": ["a) sequence", "b) decision"], "ans": "a"},
        {"q": "Loops reduce?", "options": ["a) repetition", "b) speed"], "ans": "a"}
    ],

    "practice": [
        "Print 1 to 10.",
        "Print even numbers.",
        "Sum of first 10 numbers.",
        "Multiplication table.",
        "Reverse number.",
        "Count digits.",
        "Print pattern.",
        "Factorial using loop.",
        "Fibonacci series.",
        "Explain break & continue."
    ]
}
