**Notice: I have changed the format of submissions for the challenge, to make it easier to understand. Existing submissions do not need to be updated—the controller supports the legacy format—but please make new submissions with the new, one-function format.**

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

Each round, your bot decides how far it is willing to cooperatively count with its opponent.

## Possible outcomes

**One player stops counting before the other**

The player who stopped counting first is awarded twice as many points as the value they counted up to. The other player gains no points.

**Both you and your opponent stop counting at the same time**

Neither of you gain any points.

**Both you and your opponent count all the way to 100**

Each player gains 100 points.

## Example

- Player 1: decides to count to 80
- Player 2: decides to count to 30

Player 2 gets 60 points, player 1 gets 0 points.

-----

In another round:

- Player 1: decides to count to 57
- Player 2: decides to count to 57

Neither player gets points.

-----

In yet another round:

- Player 1: decides to count to 100
- Player 2: decides to count to 100

Each player gets 100 points.

# Overall game flow

Your bot will be matched against other bots. It will play some number of rounds in a row, `n`, against the same bot.
`n` will be somewhere in the range of 100 - 1000. This allows your bot to adapt to the other bot's strategy.

# Winning the KOTH

Each bot will have a go against each other bot. Your bot can win in two categories:

- **Score:** the total scores will be summed and the bot with the most points at the end will win.
- **Wins:** a 'win' is counted for the bot with the highest score after the `n` rounds have been played.

# Technical details


Write **one** function in Python 3 with this signature:

```py
def strategy(last_results: list[tuple[int, bool]]) -> int
```

- `strategy` is called once at the beginning of each round. 
  - `last_results` is a list of previous results against the same opponent. Each item in the list is the result of a round in the form `(value reached, won)`, where `won` denotes whether the player
won or not. If the player won through cooperation, this will be `True`.
  - e.g.: if you lose your first round because your opponent stops counting at 79, `last_results` looks like `[(79, False)]` at the start of round 2. If you then win round 2 by stopping counting at 34, `last_results` will look like `[(79, False), (34, True)]` at the start of round 3.
  - `strategy` should return the value at which the bot will stop counting. `1` stops counting immediately, `100` is an agreement to count cooperatively with the other bot all the way to the end, and e.g. `47` will stop counting when the value is `47`, earning the bot 84 points.

## Example bot

'Naiive' counts up to one before the number that was reached last round if it lost, otherwise it counts up to and including the number it won on.

```py
def strategy(last_games):
    if len(last_games) == 0:
        return 100,
    
    # Count up to one before the last number that was counted if we lost,
    # otherwise just up to the last number that was counted.
    if last_games[-1][1]:
        return last_games[-1][0]
    else:
        return last_games[-1][0] - 1
```

## Legacy format (don't use)

**I've decided on a simpler format since the last one was causing confusion. Here is the old one for reference purposes. New submissions should be in the new format. Submissions using the legacy format do not need to update their submission.**

```py
# Don't use this, see above
def strategy(last_results: list[tuple[int, bool]]) -> tuple:
    pass

def turn(current_value: int, *args) -> bool:
    pass
```

# Rules

- No cheating by interfering directly with your opponent (through global variables etc.).
- Your function should be relatively quick to execute - the quicker it is, the better.
- You *may* submit multiple entries.
- Submissions close a week from the start of this post, at 2021-04-17 11:00 UTC

# Controller, sandbox, arena

**The controller is available at [https://github.com/jthistle/KOTH-counting](https://github.com/jthistle/KOTH-counting).**

A couple of example bots are provided along with it to demonstrate how to use it.

`sandbox.py` provides a place to try out your bot against others and debug it.

`arena.py` is what I'll be using to calculate final scores. It pits each bot against each other bot.
