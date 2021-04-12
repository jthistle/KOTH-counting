# Author: Wezl
# https://codegolf.stackexchange.com/a/223241

def strategy(last_results):
  if not last_results:
    return 47
  return max(1, min(50, sum(map(lambda t: t[0], last_results)) // (len(last_results)*1.5)))
