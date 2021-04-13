# Author: Leo
# https://codegolf.stackexchange.com/a/223363

def strategy(last_results):
    previous_values = list()
    diffs = list()
    for num,result in last_results:
        if result:
            oppo_play = min(100,num+1)
        else:
            oppo_play = num
        if len(previous_values)>0:
            diffs.append(oppo_play-previous_values[-1])
        previous_values.append(oppo_play)

    if len(previous_values) == 0:
        move = 100
    elif len(previous_values) == 1:
        move = previous_values[0]
    else:
        diffs = diffs[-10:]
        if len(diffs)>2:
            # remove outliers
            diffs.remove(min(diffs))
            diffs.remove(max(diffs))
        meandiff = sum(diffs)/len(diffs)
        move = previous_values[-1] + meandiff -1

    if move==99 and len(last_results)<950:
        # Let's be nice (for a while)
        move=100
    return min(100, max(1, round(move)))
