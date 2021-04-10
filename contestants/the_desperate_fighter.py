# Author: Wasif
# https://codegolf.stackexchange.com/a/223206

def strategy(last_results):
    if len(last_results) == 0:
      return True,
    pos = last_results[-1][0]
    if pos in [49,50]:
      return False,
    if pos in list(range(10,21)):
      return False,
    else:
      return True,

def turn(current_value, *args):
    return args[0]
