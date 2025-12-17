# main.py

from levels import get_level
from scoreboard import add_score, show_score, get_score

def load_topic(topic_no):
    module_name = f"topics.topic{topic_no:02d}"
    module = __import__(module_name, fromlist=["TOPIC"])
    return module.TOPIC

def show_navigation(topic_no):
    print("\n--- Navigation ---")
    if topic_no > 1:
        print("P - Previous Topic")
    if topic_no < 30:
        print("N - Next Topic")
    print("H - Home")
    print("E - Exit")
    return input("Choose option: ").lower()

def generate_certificate(level):
    filename = f"{level.lower()}_certificate.txt"
    with open(filename, "w") as f:
        f.write("PYTHON COURSE CERTIFICATE\n")
        f.write("==========================\n")
        f.write(f"Level Completed : {level}\n")
        f.write(f"Final Score     : {get_score()}\n")
        f.write("Status          : PASSED\n")
    print(f"\n🎉 Certificate generated: {filename}")

def run_quiz(topic):
    score = 0
    print("\n--- QUIZ ---")

    for q in topic["mcqs"]:
        print("\n" + q["q"])
        for opt in q["options"]:
            print(opt)
        ans = input("Answer: ").strip().lower()
        if ans == q["ans"]:
            score += 10

    print("Quiz Score:", score)
    return score

def run_practice(topic):
    print("\n--- PRACTICE QUESTIONS ---")
    for i, q in enumerate(topic["practice"], 1):
        print(f"{i}. {q}")

def main():
    topic_no = 1

    while True:
        print("\n==============================")
        print(" PYTHON MASTER LEARNING SYSTEM ")
        print("==============================")
        print("Select Topic (1–30)")
        print("0 - Exit")

        try:
            choice = input("Enter choice (press Enter to continue current topic): ").strip()
            if choice == "0":
                print("Thank you for learning Python 🙏")
                break
            if choice:
                topic_no = int(choice)
        except:
            print("Invalid input")
            continue

        if not (1 <= topic_no <= 30):
            print("Please select topic between 1 and 30")
            continue

        topic = load_topic(topic_no)
        level = get_level(topic_no)

        print("\n================================")
        print(f"Topic {topic_no}: {topic['title']}")
        print("Level:", level)
        print("================================")

        print("\n--- DESCRIPTION ---")
        for line in topic["description"]:
            print("-", line)

        print("\n--- SAMPLE PROGRAMS ---")
        for p in topic["programs"]:
            print("\nCode:\n" + p["code"])
            print("Explanation:", p["explanation"])

        score = run_quiz(topic)
        add_score(score)

        choice = input("\nDo you want practice questions? (yes/no): ").lower()
        if choice == "yes":
            run_practice(topic)

        show_score()

        # Certificate checkpoints
        if topic_no == 10:
            generate_certificate("Beginner")
        elif topic_no == 20:
            generate_certificate("Intermediate")
        elif topic_no == 30:
            generate_certificate("Advanced")

        nav = show_navigation(topic_no)

        if nav == "n" and topic_no < 30:
            topic_no += 1
        elif nav == "p" and topic_no > 1:
            topic_no -= 1
        elif nav == "h":
            topic_no = 1
        elif nav == "e":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()
