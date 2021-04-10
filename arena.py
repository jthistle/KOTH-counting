#!/usr/bin/env python3

from controller import Controller

from contestants import example_random
from contestants import example_naiive
from contestants import dedicated
from contestants import primitive
# from contestants import desperate
from contestants import shortcut
from contestants import crab

# Format: name, strategy function, (legacy only) turn function 
contestants = [
    ("Random", example_random.strategy),
    ("Naiive", example_naiive.strategy),
    ("The Dedicated Counter", dedicated.strategy, dedicated.turn),
    ("The Primitive Looker", primitive.strategy, primitive.turn),
    ("Shortcut", shortcut.strategy, shortcut.turn),
    ("Crab", crab.strategy, crab.turn),
    # ("The Desperate Fighter", desperate.strategy, desperate.turn),
]

scores = [0] * len(contestants)
wins = [0] * len(contestants)

N_GAMES = 1000

for i in range(len(contestants)):
    for j in range(i):
        contestant = contestants[i]
        opponent = contestants[j]
        if contestant == opponent:
            continue

        ctrl = Controller(contestant[1:], opponent[1:])

        result = ctrl.run(N_GAMES)

        scores[i] += result[0]
        scores[j] += result[1]

        if result[0] > result[1]:
            wins[i] += 1
        elif result[0] < result[1]:
            wins[j] += 1

ordered_score = sorted(zip(contestants, scores), key=lambda x: x[1], reverse=True)
ordered_wins = sorted(zip(contestants, wins), key=lambda x: x[1], reverse=True)

print("By score:")
for i in range(len(contestants)):
    print(f"{i + 1}: {ordered_score[i][0][0]} with {ordered_score[i][1]} points")

print("\nBy wins:")
for i in range(len(contestants)):
    print(f"{i + 1}: {ordered_wins[i][0][0]} with {ordered_wins[i][1]}/{len(contestants) - 1} wins")
