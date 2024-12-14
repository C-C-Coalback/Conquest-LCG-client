from PassCommand import check_for_pass
from ActionChecker import check_for_action
from RefreshChecker import check_for_refresh


def determine_choice_pos_in_lobby(coord1, coord2):
    x = coord1
    y = coord2
    if 300 < x < 440:
        y = y - 100
        remainder = y % 50
        if remainder < 33:
            y = int(y / 50)
            return y
    return -1


def determine_accept_game(x, y):
    if 800 < x < 890 and 250 < y < 282:
        return "a"
    elif 920 < x < 1010 and 250 < y < 282:
        return "r"
    return ""


def pos_from_click(x, y, mode, invitee, current_lobby=None):
    message = ""
    if mode == "Lobby":
        if check_for_refresh(x, y):
            return "REQUEST LOBBY"
        if invitee != "":
            a_or_r = determine_accept_game(x, y)
            if a_or_r == "a":
                return "START GAME#" + invitee
            if a_or_r == "r":
                return "REFUSE REQUEST#" + invitee
            return ""
        pos = determine_choice_pos_in_lobby(x, y)
        if current_lobby is not None:
            if len(current_lobby) > pos != -1:
                message = "REQUEST MATCH#" + current_lobby[pos]
                return message
        return ""
    if check_for_pass(x, y):
        return "PASS"
    if check_for_action(x, y):
        return "ACTION"

    if 319 < y < 376:  # PLANETS
        position = x - 60
        remainder = position % 165
        position = int(position / 165)
        if 84 < remainder:
            return message
        else:
            message = "Planet#" + str(position)
            return message
    if 500 < y < 588:  # HQ PLAYER ONE
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        if 62 < remainder:
            return ""
        else:
            message = "P1#HQ#" + str(position)
            return message
    if 125 < y < 213:  # HQ PLAYER TWO
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        if 62 < remainder:
            return ""
        else:
            message = "P2#HQ#" + str(position)
            return message
    if 594 < y < 686:  # HAND PLAYER ONE
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
    if 24 < y < 116:  # HAND PLAYER TWO
        position = x
        position = position - 200
        remainder = position % 80
        position = int(position / 80)
        if 62 < remainder:
            return ""
        else:
            message = "P2#Hand#" + str(position)
            return message
    if y > 385:  # IN PLAY PLAYER ONE
        x_pos = x % 165
        if 60 < x_pos < 185:
            position = y
            position = position - 385
            position = int(position / 88)
            position = 2 * position
            if x_pos > 122:
                position = position + 1
            planet_pos = x - 60
            planet_pos = int(planet_pos / 165)
            message = "P1#PLAY#" + str(planet_pos) + "#" + str(position)
            return message
        return ""
    if y < 320:  # IN PLAY PLAYER ONE
        x_pos = x % 165
        if 60 < x_pos < 185:
            position = y
            position = position - 320
            position = -1 * position
            position = int(position / 88)
            position = 2 * position
            if x_pos > 122:
                position = position + 1
            planet_pos = x - 60
            planet_pos = int(planet_pos / 165)
            message = "P2#PLAY#" + str(planet_pos) + "#" + str(position)
            return message
        return ""
    return message
