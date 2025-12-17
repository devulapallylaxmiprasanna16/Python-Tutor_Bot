# levels.py

def get_level(topic_no):
    if 1 <= topic_no <= 10:
        return "Beginner"
    elif 11 <= topic_no <= 20:
        return "Intermediate"
    elif 21 <= topic_no <= 30:
        return "Advanced"
    else:
        return "Unknown"
