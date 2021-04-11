#!/usr/bin/env python3

# Many thanks to original author RedwolfPrograms

import requests
import re
import os
from urllib.parse import unquote
from html import unescape

if not os.path.isdir("contestants"):
    raise "contestantsn't"

for f in os.listdir("contestants"):
    if not os.path.isdir("contestants/" + f):
        os.remove("contestants/" + f)


BLACKLIST = [
    223247, # Copycat, until usage of only one strat per tournament is confirmed
]

has_more = True
answers = []
while has_more:
    response = requests.get("https://api.stackexchange.com/2.2/questions/223202/answers?site=codegolf&filter=!bN4iJhwDifN*s1")

    if response.status_code != 200:
        raise response.status_code

    json = response.json()
    has_more = json["has_more"]

    answers.extend(json["items"])

arena_imports = []
arena_list = []

for a in answers:
    if a["body"][:4] != "<h1>" and a["body"][:4] != "<h2>":
        raise "namen't"

    if int(a["answer_id"]) in BLACKLIST:
        continue

    name = a["body"][4:a["body"].index("</h" + a["body"][2] + ">")]

    start = a["body"].index("<code>")
    finish = a["body"].index("</code>")

    program = "# Author: {}\n".format(a["owner"]["display_name"])
    program += "# https://codegolf.stackexchange.com/a/{num}\n\n".format(num=a["answer_id"])
    program += unescape(a["body"][start + 6:finish])

    short_name = re.sub(r"[^a-z0-9]+", "_", name.lower())

    with open("contestants/" + short_name + ".py", "w") as file:
        file.write(program)

    arena_imports.append("from contestants import " + short_name)

    if program.find("def turn") == -1:
        arena_list.append("    (\"" + name + "\", " + short_name + ".strategy),")
    else:
        # Legacy
        arena_list.append("    (\"" + name + "\", " + short_name + ".strategy, " + short_name + ".turn),")


with open("arena.py", "r") as arena:
    old = arena.read()
    arena.close()

old_lines = old.splitlines()
start = old_lines.index("# Begin autogenerate") + 1
end = old_lines.index("# End autogenerate")
new_lines = old_lines[:start] + arena_imports + ["", "contestants = ["] + arena_list + ["]"] + old_lines[end:]

with open("arena.py", "w") as arena:
    arena.write("\n".join(new_lines))
