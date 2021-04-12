# Author: caird coinheringaahing
# https://codegolf.stackexchange.com/a/223347

def strategy(last_results):
        scores = list(map(lambda a: a[0], last_results))

        if all(score == 100 for score in scores):
                if len(scores) == 999:
                        return 98
                return 100

        constant_bots = {
                69: 68,
                68: 67,
                50: 49,
                48: 47
        }

        return constant_bots.get(scores[-1], 1)
