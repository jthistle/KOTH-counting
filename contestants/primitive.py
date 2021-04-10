# https://codegolf.stackexchange.com/a/223207/102975

import random

def strategy(last_results):
    num = random.randint(10, 20)

    try:
        return (last_results[len(last_results)-1][1], )
    except:
        return (False, )

def turn(current_value, won):
    if won:
        if current_value == 99:
            c = False
        else:
            c = True
    else:
        if current_value == 27:
            c = False
        else:
            c = True

    return c