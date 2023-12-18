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

import re
# %%
#%%
puzzle = p.get_puzzle()
# %%
txt = p.get_data(-1, [
    """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
])

def find_start(y,x):
    global map_v
    if not re.match("\d",map_v[y][x]):
        return None
    while re.match("\d",map_v[y][x]) and x>0:
        x-=1
    return y,x

map_v = txt.splitlines()
sum_v = 0
chars = set()
for i, r in enumerate(map_v):
    for j, c in enumerate(r):
        if c == ".": continue
        if re.match("\d", c): continue


        if i>0:
            chars.add(find_start(i-1,j))
        if j>0:
            chars.add(find_start( i, j-1))
        if j>0 and i>0:
            chars.add(find_start( i-1, j-1))
        if i<len(map_v)-1:
            chars.add(find_start( i+1, j))
        if j<len(r)-1:
            chars.add(find_start( i, j+1))
        if i<len(map_v)-1 and j<len(r)-1:
            chars.add(find_start( i+1, j+1))
        if i<len(map_v)-1 and j>0:
            chars.add(find_start( i+1, j-1))
        if i>0 and j<len(r)-1:
            chars.add(find_start( i-1, j+1))
# print(chars)
# sum_v += sum(p.get_ints(".".join(chars)))
# sum_v
# %%
# chars.remove(None)
sum_v = 0
for y,x in sorted(chars):
    v=p.get_ints(map_v[y][x:])[0]
    print(v)
    sum_v += v
sum_v
# %%
map_v = txt.splitlines()
sum_v = 0
for i, r in enumerate(map_v):
    for j, c in enumerate(r):
        if c != "*": continue
        if re.match("\d", c): continue

        chars = set()
        if i>0:
            chars.add(find_start(i-1,j))
        if j>0:
            chars.add(find_start( i, j-1))
        if j>0 and i>0:
            chars.add(find_start( i-1, j-1))
        if i<len(map_v)-1:
            chars.add(find_start( i+1, j))
        if j<len(r)-1:
            chars.add(find_start( i, j+1))
        if i<len(map_v)-1 and j<len(r)-1:
            chars.add(find_start( i+1, j+1))
        if i<len(map_v)-1 and j>0:
            chars.add(find_start( i+1, j-1))
        if i>0 and j<len(r)-1:
            chars.add(find_start( i-1, j+1))
        if None in chars:
            chars.remove(None)
        if len(chars) != 2: continue
        chars = list(chars)
        y,x = chars[0]
        v1 = p.get_ints(map_v[y][x:])[0]
        y,x = chars[1]
        v2 = p.get_ints(map_v[y][x:])[0]
        sum_v += v1*v2