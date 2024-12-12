from PassCommand import check_for_pass
from ActionChecker import check_for_action

def pos_from_click(x, y):
    message = ""
    if check_for_pass(x, y):
        return "PASS"
    if check_for_action(x, y):
        return "ACTION"
    if 319 < y < 376:
        position = x - 60
        remainder = position % 165
        position = int(position / 165)
        if 84 < remainder:
            pass
        else:
            message = "Planet#" + str(position)
            return message

    return message