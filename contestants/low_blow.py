# Author: caird coinheringaahing
# https://codegolf.stackexchange.com/a/223223

import random
import statistics

def strategy(last_results):
        scores = list(map(lambda a: a[0], last_results))
        if not scores: return 99

        if len(scores) > 420 and scores[:3] == [69, 68, 68]:
                return 67

        decrements = [50, 69, 48]

        if all(score == 1 for score in scores): return 1

        for decrement in decrements:
                mold = [decrement]
                for _ in scores[1:]: mold.append(decrement - 1)
                if scores == mold:
                        return decrement - 1

        if scores[0] == 65:
                if scores[-1] == 1: return 1
                return random.randint(1, 48)

        if scores == [98]:
                return 97

        if len(scores) == 1 and scores[0] < 48:
                return scores[0]

        if last_results[:2] == [(99, True), (99, False)]:
                return max(scores[-1] - 1, 1)

        if scores[:2] == [47, 31]    : return max(min(50, int(sum(scores) / (len(scores) * 1.5))) - 1, 1)
        if scores[:2] == [99, 97]    : return max(scores[-1] - 3, 1)
        if scores[:2] == [99, 98]    : return max(scores[-1] - 2, 1)
        if scores[:3] == [99, 99, 98]: return max(scores[-1] - 1, 1)

        if scores[:2] == [98, 97]    :
                htl_losses = [result[0] for result in last_results if result[1]]
                return max(min(htl_losses) - len(htl_losses) - 2, 1)

        if len(scores) > 1 and scores[0] == scores[1] != 99:
                mean = round(statistics.mean(scores))
                median = round(statistics.median(sorted(scores)))

                if mean == median:
                        return max(mean - 1, 1)
                return max(abs(median - mean) - 1, 1)

        if scores[-1] == 1:
                return 1

        if len(scores) <= 3: return 99

        deltas = [scores[~0] - scores[~1], scores[~1] - scores[~2]]
        if any(deltas): return random.randint(37, 50)

        return 99
