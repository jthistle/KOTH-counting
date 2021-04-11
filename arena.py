#!/usr/bin/env python3

from controller import Controller

from example_contestants import naiive
from example_contestants import random

# Begin autogenerate
from contestants import hawk
from contestants import low_blow
from contestants import zoidberg
from contestants import simple_killer
from contestants import the_primitive_looker
from contestants import hard_coded
from contestants import funnynumber
from contestants import the_desperate_fighter
from contestants import crab
from contestants import shortcut
from contestants import the_dedicated_counter

contestants = [
    ("Hawk", hawk.strategy),
    ("Low Blow", low_blow.strategy),
    ("Zoidberg", zoidberg.strategy),
    ("Simple Killer", simple_killer.strategy),
    ("The primitive looker", the_primitive_looker.strategy, the_primitive_looker.turn),
    ("Hard-coded", hard_coded.strategy),
    ("FunnyNumber", funnynumber.strategy),
    ("The Desperate Fighter", the_desperate_fighter.strategy, the_desperate_fighter.turn),
    ("Crab", crab.strategy),
    ("Shortcut", shortcut.strategy, shortcut.turn),
    ("The dedicated counter", the_dedicated_counter.strategy, the_dedicated_counter.turn),
]
# End autogenerate

contestants += [
    ("Naiive", naiive.strategy),
    ("Random", random.strategy),
]

# Contestants list has format: name, strategy function, (legacy only) turn function 

scores = [0] * len(contestants)
wins = [0] * len(contestants)

N_GAMES = 1000

for i in range(len(contestants)):
    for j in range(i):
        contestant = contestants[i]
        opponent = contestants[j]
        if contestant == opponent:
            continue

        ctrl = Controller(contestant[1:], opponent[1:], (contestant[0], opponent[0]))

        result = ctrl.run(N_GAMES)

        scores[i] += result[0]
        scores[j] += result[1]

        if result[0] > result[1]:
            wins[i] += 1
        elif result[0] < result[1]:
            wins[j] += 1

ordered_score = sorted(zip(contestants, scores), key=lambda x: x[1], reverse=True)
ordered_wins = sorted(zip(contestants, wins), key=lambda x: x[1], reverse=True)

overall = {}


def joint_rank(sorted_list, key):
    last = -1
    rank = 0
    buffer = 0
    out = []
    for item in sorted_list:
        score = key(item)
        if score != last:
            rank += buffer + 1
            buffer = 0
        else:
            buffer += 1
        out.append((item, rank))
        last = score

    return out


print("By score:")
for (contestant, points), rank in joint_rank(ordered_score, key=lambda x: x[1]):
    print(f"{rank}: {contestant[0]} with {points} points")
    overall[contestant] = rank

print("\nBy wins:")
for (contestant, wins), rank in joint_rank(ordered_wins, key=lambda x: x[1]):
    print(f"{rank}: {contestant[0]} with {wins}/{len(contestants) - 1} wins")
    overall[contestant] += rank

# Calculate combined
ordered_overall = [(c, overall[c]) for c in sorted(overall.keys(), key=lambda x: overall[x])]

print("\nCombined leaderboard (fewer pts = better):")
for (contestant, score), rank in joint_rank(ordered_overall, key=lambda x: x[1]):
    print(f"{rank}: {contestant[0]}  ({score} pts)")