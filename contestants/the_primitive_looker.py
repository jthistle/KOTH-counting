# Author: math
# https://codegolf.stackexchange.com/a/223207

def strategy(last_results):
    if not last_results:
        return 100
    if any(not x[1] for x in last_results):
        if last_results[-1][0] - 2 > 0:
            return last_results[-1][0] - 2
        return 100
    return 99
