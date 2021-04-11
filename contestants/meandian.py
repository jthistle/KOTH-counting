# Author: Aiden4
# https://codegolf.stackexchange.com/a/223287

import random
import statistics as stats
def strategy(last_results):
    def clamp(minimum, x, maximum):
        return max(minimum, min(x, maximum))
    if not len(last_results):
        return random.randint(1,47)
    else:
        last_results = list(map(lambda a:a[0], last_results))
        last_results.sort()
        mean = round(stats.mean(last_results))
        median = round(stats.median(last_results))
    if mean == median:
        return mean
    elif mean > median:
        return clamp(1, median - random.randint(1,mean - median), 100)
    else: 
        return clamp(1, mean - random.randint(1,median - mean), 100)

