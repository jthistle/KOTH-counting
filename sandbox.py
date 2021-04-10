#!/usr/bin/env python3

from contestants import example_random
from contestants import example_naiive

from controller import Controller

ctrl = Controller(
    [example_random.strategy],
    [example_naiive.strategy],
)

# Run games
ctrl.run(1000, debug=True)
