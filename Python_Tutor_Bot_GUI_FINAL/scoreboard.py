# scoreboard.py

_total_score = 0

def add_score(score):
    global _total_score
    _total_score += score

def get_score():
    return _total_score

def show_score():
    print("\n========================")
    print("TOTAL SCORE :", _total_score)
    print("========================")
