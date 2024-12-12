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
            return message
        else:
            message = "Planet#" + str(position)
            return message
    if 500 < y < 588:
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        if 62 < remainder:
            return ""
        else:
            message = "P1#HQ#" + str(position)
    if 125 < y < 213:
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        if 62 < remainder:
            return ""
        else:
            message = "P2#HQ#" + str(position)

    return message