# Author: Neil
# https://codegolf.stackexchange.com/a/223290

def strategy(last_results):
    return last_results[-1][0] if last_results else 100
