#!/usr/bin/env python3

from controller import Controller

from example_contestants import naiive
from example_contestants import random

# Begin autogenerate
from contestants import simple_killer
from contestants import the_primitive_looker
from contestants import hard_coded
from contestants import low_blow
from contestants import funnynumber
from contestants import the_desperate_fighter
from contestants import crab
from contestants import shortcut
from contestants import the_dedicated_counter

contestants = [
    ("Simple Killer", simple_killer.strategy),
    ("The primitive looker", the_primitive_looker.strategy, the_primitive_looker.turn),
    ("Hard-coded", hard_coded.strategy),
    ("Low Blow", low_blow.strategy),
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
ordered_all = sorted(contestants, key=lambda x: [y[0] for y in ordered_score].index(x) + [y[0] for y in ordered_wins].index(x))

print("By score:")
for i in range(len(contestants)):
    print(f"{i + 1}: {ordered_score[i][0][0]} with {ordered_score[i][1]} points")

print("\nBy wins:")
for i in range(len(contestants)):
    print(f"{i + 1}: {ordered_wins[i][0][0]} with {ordered_wins[i][1]}/{len(contestants) - 1} wins")

print("\nCombined leaderboard:")
for i in range(len(contestants)):
    print(f"{i + 1}: {ordered_all[i][0]}")