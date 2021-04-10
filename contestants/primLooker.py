import random

res = []
num = 0

def strategy(last_results):
    global res, num
    res = last_results
    num = random.randint(10, 20)    
        
    return ()

def turn(current_value, *args):
    if len(res) >= 1:
        won = res[len(res)-1][1]
        if won:
            if current_value == 99:
                c = False
            else:
                c = True
        else:
            if current_value == num:
                c = False
            else:
                c = True
    else:
        c = False

    return c
