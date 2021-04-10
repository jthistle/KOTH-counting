
def strategy(last_games):
    if len(last_games) == 0:
        return 100
    
    # Count up to one before the last number that was counted if we lost,
    # otherwise just up to the last number that was counted.
    if last_games[-1][1]:
        return last_games[-1][0]
    else:
        return last_games[-1][0] - 1