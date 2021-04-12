# Author: Spitemaster
# https://codegolf.stackexchange.com/a/223224

def strategy(last_results):
    if not len(last_results):
        return 100
    if len(last_results) == 999 and last_results[-1][0] == 100:
        return 99
    last_move = last_results[-1]
    if last_move in last_results[:-1]:
        pos = last_results.index(last_move)
        if last_results[pos + 1][1]:
            return last_results[pos + 1][0]
        return max(last_results[pos + 1][0] - 1, 1)
    return 100
