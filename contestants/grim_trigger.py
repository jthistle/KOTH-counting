# Author: qwatry
# https://codegolf.stackexchange.com/a/223337

def strategy(last_results):
    if any([not r[1] for r in last_results]):
        return 1
    else:
        return 100
