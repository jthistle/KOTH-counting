# Author: qwatry
# https://codegolf.stackexchange.com/a/223342

def strategy(last_results):
    if last_results:
        losses = [r[0] for r in last_results if not r[1]]
        if losses:
            return max(1, min(losses)-1-len(losses))
        num_of_rounds = len(last_results)
        if num_of_rounds>15 and len(losses)/num_of_rounds>0.6:
            return 1
    return 98
