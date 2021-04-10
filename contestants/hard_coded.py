# Author: Wasif
# https://codegolf.stackexchange.com/a/223222

import random
def strategy(last_results):
  if len(last_results) == 0:
    return 65
  if last_results[-1][0] in [50,49]:
    return 49 # Shortcut detected, attack!
  if last_results[-1][0] in [69,65]:
    return 65 # FunnyNumber detected, attack!
  if last_results[-1][0]==1:
    return 1 # Crab detected, defend!
  else:
    return random.randint(1,100) # give away, my mind is boggling with numbers
