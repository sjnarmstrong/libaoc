#%%
import sys
sys.path.append("../../..")
from aocd.utils import http

http.pool_manager.connection_pool_kw["cert_reqs"] = 'CERT_NONE'

from libaoc import parse as p, util, vec
from itertools import combinations
import math
import re
import numpy as np
from collections import Counter
# %%
#%%
puzzle = p.get_puzzle()
# %%
txt = p.get_data(-1, [
    """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
])

import re

colors = {
    "red":12,
    "green":13,
    "blue":14,
}

def ismatch(data):
    for d in data:
        for num, colour in re.findall("(\d+) (\w*)", d):
            num = int(num)
            # print(num, colour)
            if num > colors[colour]:
                return False
    return True
sum_v =0
for ln in txt.splitlines():
    game, data = ln.split(":")
    data = data.split(";")
    game_no = p.get_ints(game)[0]
    if ismatch(data):
        # print(game_no)
        sum_v += game_no
sum_v
# %%
txt = p.get_data(-1, [
    """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
])

import re

colors = {
    "red":0,
    "green":1,
    "blue":2,
}

def ismatch(data):
    v = [0,0,0]
    for d in data:
        for num, colour in re.findall("(\d+) (\w*)", d):
            num = int(num)
            v[colors[colour]] = max(v[colors[colour]],num)
    return v[0]*v[1]*v[2]

sum_v =0
all_vs: list[vec.Vec] = []
for ln in txt.splitlines():
    game, data = ln.split(":")
    data = data.split(";")
    game_no = p.get_ints(game)[0]
    all_vs.append(ismatch(data))
from functools import reduce
sum(all_vs)
# %%
