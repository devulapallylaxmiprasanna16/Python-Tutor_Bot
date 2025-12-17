def navigation_menu(topic_no):
    print("\nNavigation:")
    if topic_no > 1:
        print("P - Previous Topic")
    if topic_no < 30:
        print("N - Next Topic")
    print("H - Home")
    print("E - Exit")

    return input("Choose: ").lower()
