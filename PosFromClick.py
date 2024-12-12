from PassCommand import check_for_pass
from ActionChecker import check_for_action

def pos_from_click(x, y):
    message = ""
    if check_for_pass(x, y):
        return "PASS"
    if check_for_action(x, y):
        return "ACTION"
    if 319 < y < 376: #PLANETS
        position = x - 60
        remainder = position % 165
        position = int(position / 165)
        if 84 < remainder:
            return message
        else:
            message = "Planet#" + str(position)
            return message
    if 500 < y < 588: #HQ PLAYER ONE
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        if 62 < remainder:
            return ""
        else:
            message = "P1#HQ#" + str(position)
            return message
    if 125 < y < 213: #HQ PLAYER TWO
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        if 62 < remainder:
            return ""
        else:
            message = "P2#HQ#" + str(position)
            return message
    if 594 < y < 686:
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        print(position, remainder)
        if 62 < remainder:
            return ""
        else:
            message = "P1#Hand#" + str(position)
            return message
    if 24 < y < 116:
        position = x
        position = position - 200
        remainder = position % 80
        position = int(position / 80)
        if 62 < remainder:
            return ""
        else:
            message = "P2#Hand#" + str(position)
            return message

    return message