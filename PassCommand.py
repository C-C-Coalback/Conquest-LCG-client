def check_for_pass(x, y):
    if 1100 < x < 1200 and 600 < y < 650:
        print("player one pass")
        return 1
    if 0 < x < 100 and 0 < y < 50:
        print("player two pass")
        return 1
    return 0
