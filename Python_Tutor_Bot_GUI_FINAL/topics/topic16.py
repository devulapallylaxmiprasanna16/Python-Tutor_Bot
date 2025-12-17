# topic16.py
# Topic 16 : File Handling
# Level : Intermediate

TOPIC = {
    "number": 16,
    "title": "File Handling",

    "description": [
        "File handling is used to store data permanently.",
        "Files can be opened using open() function.",
        "Read mode is used to read file content.",
        "Write mode overwrites file content.",
        "Append mode adds data to file.",
        "Files must be closed after use.",
        "with statement auto-closes file.",
        "Text and binary files exist.",
        "Used in real-world applications.",
        "Very important concept."
    ],

    "programs": [
        {
            "code": "f = open('data.txt','w')\nf.write('Hello Python')\nf.close()",
            "explanation": "Creates a file and writes data."
        },
        {
            "code": "f = open('data.txt','r')\nprint(f.read())\nf.close()",
            "explanation": "Reads content from a file."
        }
    ],

    "mcqs": [
        {"q": "Function to open file?", "options": ["a) open()", "b) file()"], "ans": "a"},
        {"q": "Mode to read file?", "options": ["a) r", "b) w"], "ans": "a"},
        {"q": "Mode to write file?", "options": ["a) w", "b) r"], "ans": "a"},
        {"q": "Append mode?", "options": ["a) a", "b) b"], "ans": "a"},
        {"q": "Must close file?", "options": ["a) Yes", "b) No"], "ans": "a"},
        {"q": "with statement does?", "options": ["a) Auto close", "b) Delete"], "ans": "a"},
        {"q": "Text file extension?", "options": ["a) .txt", "b) .exe"], "ans": "a"},
        {"q": "Binary file mode?", "options": ["a) rb", "b) r"], "ans": "a"},
        {"q": "File used for?", "options": ["a) Permanent storage", "b) Temporary"], "ans": "a"},
        {"q": "File handling used in?", "options": ["a) Real apps", "b) Comments"], "ans": "a"}
    ],

    "practice": [
        "Create text file.",
        "Write data to file.",
        "Read file data.",
        "Append data.",
        "Use with statement.",
        "Count file lines.",
        "Copy file content.",
        "Store user data.",
        "Delete file content.",
        "Explain file modes."
    ]
}
