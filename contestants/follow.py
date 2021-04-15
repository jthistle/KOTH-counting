# Author: gsitcia
# https://codegolf.stackexchange.com/a/223360

def strategy(last_results):
    n = len(last_results)
    if n == 0: return 100
    if all(i == (1,False) for i in last_results): return 2 # nice to the crab
    a,b = last_results[-1]
    if n == 1:
        if b: return 100
        return 1+int(.97*(a-1))
    c,d = last_results[-2]
    if n >= 99 and a == 100: return 99
    if b and d: # won previous two rounds
        if (a+1,False) not in last_results:
            return min(100,a+1)
        return a
    else:
        a,c = sorted((a,c))
        return max(1,a*a//c-1)
