from PassCommand import check_for_pass
from ActionChecker import check_for_action

def pos_from_click(x, y):
    if check_for_pass(x, y):
        return "PASS"
    if check_for_action(x, y):
        return "ACTION"
    message = str(x) + "#" + str(y)
    return message