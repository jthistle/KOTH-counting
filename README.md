# Cooperative Counting - Python 3 KOTH

Have you ever tried to count to 100 in an online forum or comment thread? It normally goes something like:

```
1
>2
>>3
>>>4
>>>>69 xD xD
```

the point being that someone will always try to ruin the fun.

# The game

This is a bit like the counting example above, except to make sure that neither player has an advantage
from going first, each player will count at the same time as the other.

Your bot will be pitted against another bot. Your goal? Cooperatively count to 100.

Each turn, your bot can do one of two things:

- count the next number in the sequence
- stop counting

## Possible outcomes

**Both you and your opponent keep counting**

The current value of the sequence increases by one.

**One person stops counting, but the other keeps counting**

The person who stopped counting is awarded twice as many points as the last value reached. The other
person gains no points. The counting sequence is reset to 0.

**Both you and your opponent stop counting**

Neither of you gain any points. The sequence resets to 0.

**At 99, both you and your opponent keep counting**

Each player gains 100 points. The sequence resets to 0.

## Example

**Value: 1**

- Player 1: keeps counting
- Player 2: keeps counting

**Value: 2**

- Player 1: keeps counting
- Player 2: keeps counting

...

**Value: 30**

- Player 1: keeps counting
- Player 2: stops counting

Player 2 gets 60 points, player 1 gets 0 points.

-----

In another round:

...

**Value: 57**

- Player 1: stops counting
- Player 2: stops counting

Neither player gets points.

-----

In yet another round:

...

**Value: 99**

- Player 1: keeps counting
- Player 2: keeps counting

Each player gets 100 points.

# Overall game flow

Your bot will be matched against other bots. It will play some number of rounds in a row, `n`, against the same bot.
`n` will be somewhere in the range of 100 - 1000. This allows your bot to adapt to the other bot's strategy.

**To clarify:**

- one **game**, between two bots, is made up of multiple **rounds**
- one **round** is made up of multiple **turns**. A round starts with the sequence at 1, and ends when a bot stops counting.
- one **turn** is simply made up of each bot deciding whether to keep counting or not

# Winning the KOTH

Each bot will have a go against each other bot. Your bot can win in two categories:

- **Score:** the total scores will be summed and the bot with the most points at the end will win.
- **Wins:** a 'win' is counted for the bot with the highest score after the `n` rounds have been played.

# Technical details

Write **two** functions in Python 3 with these signatures:

```py
def strategy(last_results: list[tuple[int, bool]]) -> tuple:
    pass

def turn(current_value: int, *args) -> bool:
    pass
```

`strategy` is called once at the beginning of each round. `last_results` is a list of previous results against the same opponent.
Each item in the list is the result of a game in the form `(value reached, won)`, where `won` denotes whether the player
won or not. If the player won through cooperation, this will be `True`.

e.g.: if you lose your first round because your opponent stops counting at 79, `last_results` looks like `[(79, False)]` at the start of turn 2. If you then win turn 2 by stopping counting at 34, `last_results` will look like `[(79, False), (34, True)]` at the start of turn 3.

`strategy` should return a tuple of static arguments that it wants to be passed to the `turn` function on each turn.

`turn` is a function called every turn. It is passed `current_value`, the current value of the counted sequence, and the arguments
returned by the `strategy` function.

`turn` returns a bool: `True` to keep counting, `False` to stop counting.

(The reason that there are two separate functions is to try to speed up overall execution time, so bots don't analyze `last_results` every turn.) 

# Rules

- No cheating by interfering directly with your opponent (through global variables etc.).
- Your function should be relatively quick to execute - the quicker it is, the better.
- You *may* submit multiple entries.

# Controller, sandbox, arena

**The controller is available at [https://github.com/jthistle/KOTH-counting](https://github.com/jthistle/KOTH-counting).**

A couple of example bots are provided along with it to demonstrate how to use it.

`sandbox.py` provides a place to try out your bot against others and debug it.

`arena.py` is what I'll be using to calculate final scores. It pits each bot against each other bot.
