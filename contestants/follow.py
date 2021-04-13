# Author: gsitcia
# https://codegolf.stackexchange.com/a/223360

def strategy(last_results):
    n = len(last_results)
    if n == 0: return 100
    if last_results[0][0] == 1: return 2 # nice to the crab
    a,b = last_results[-1]
    if n >= 99 and a == 100: return 99
    if b:
        if (a+1,False) not in last_results: return min(100,a+1)
        return a
    return 1+int(.97*(a-1))
