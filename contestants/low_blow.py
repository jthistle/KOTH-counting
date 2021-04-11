# Author: caird coinheringaahing
# https://codegolf.stackexchange.com/a/223223

import random

def strategy(last_results):
        scores = list(map(lambda a: a[0], last_results))
        if not scores: return 99

        if len(scores) > 420 and scores[:3] == [69, 68, 68]:
                return 67

        if scores[:3] == [50, 49, 49] and not last_results[2][1]:
                return sum(scores) // len(scores) - 1

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

        if scores[:2] == [99, 97]    : return max(scores[-1] - 3, 1)
        if len(scores) <= 3          : return 99
        if scores[:3] == [99, 98,  1]: return  1
        if scores[:3] == [99, 99, 98]: return max(scores[-1] - 1, 1)
        if scores[:3] == [99, 98, 98]: return max(scores[-1] - 2, 1)

        deltas = []
        for x, y in zip(scores, scores[1:]):
                deltas.append(x - y)

        if deltas[:3] == [2, -2, 2]: return max(scores[-1] - 3, 1)
        if deltas   and any(deltas): return random.randint(37, 50)

        return 99
