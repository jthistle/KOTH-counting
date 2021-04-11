# Author: math
# https://codegolf.stackexchange.com/a/223207

import random

def strategy(last_results):
    try:
        return (last_results, )
    except:
        return ([], )

def turn(current_value, res):
    v = 99
    m = 2
    g = True
    for i in res:
        g = g and i[1]
        
    if res == []:
        c = True
    else:
        if res[-1][1] and g:
            if current_value == v:
                c = False
            else:
                c = True
        else:
            if current_value == res[-1][0] - m:
                c = False
            else:
                c = True

    return c


