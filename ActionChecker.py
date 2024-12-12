def check_for_action(x, y):
    if 1100 < x < 1200 and 650 < y < 700:
        print("player one action")
        return 1
    if 0 < x < 100 and 50 < y < 100:
        print("player two action")
        return 1
    return 0
