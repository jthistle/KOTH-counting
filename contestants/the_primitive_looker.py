# Author: math
# https://codegolf.stackexchange.com/a/223207

def strategy(last_results):
    try:
        return (last_results, )
    except:
        return ([], )

def turn(current_value, res):
    if res == []:
        c = True
    else:
        if res[-1][1]:
            if current_value == 99:
                c = False
            else:
                c = True
        else:
            if current_value == res[-1][0] - 2:
                c = False
            else:
                c = True

        return c

