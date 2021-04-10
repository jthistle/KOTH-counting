#!/usr/bin/env python3

from example_contestants import random
from example_contestants import naiive

from controller import Controller

ctrl = Controller(
    [random.strategy],
    [naiive.strategy],
)

# Run games
ctrl.run(1000, debug=True)
