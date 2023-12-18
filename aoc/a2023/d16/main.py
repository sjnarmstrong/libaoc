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
import numpy as np
# %%
#%%
puzzle = p.get_puzzle()
# %%
from collections import defaultdict
from functools import lru_cache
from itertools import repeat, combinations, chain
txt = p.get_data(-1, [r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""])

world = txt.splitlines()
width = len(world[0])
height = len (world)


up = -1j
down = 1j
left = -1
right = 1
def get_energised_count(start, sd):
    seen = set()
    seen_w_dir = set()

    to_explore = [(start, sd)]

    while len(to_explore):
        pos, d = to_explore.pop()
        if pos.real < 0: continue
        if pos.imag < 0: continue
        if pos.real >= width: continue
        if pos.imag >= height: continue
        if (pos, d) in seen_w_dir: continue
        seen.add(pos)
        seen_w_dir.add((pos,d))
        ch = world[int(pos.imag)][int(pos.real)]
        # print(ch, d, pos)

        if ch == "|" and d.real != 0:
            to_explore.append((pos+up, up))
            to_explore.append((pos+down, down))
        elif ch == "-" and d.imag != 0:
            to_explore.append((pos+left, left))
            to_explore.append((pos+right, right))
        elif ch == "/":
            new_dir = complex(-d.imag, -d.real)
            # print(d, new_dir)
            to_explore.append((pos+new_dir, new_dir))
        elif ch == "\\":
            new_dir = complex(d.imag, d.real)
            to_explore.append((pos+new_dir, new_dir))
        else:
            to_explore.append((pos+d, d))
    return len(seen)

max_seen = 0
for i in range(height):
    max_seen = max(max_seen,get_energised_count(i, left))
    max_seen = max(max_seen,get_energised_count(i, right))
for i in range(width):
    max_seen = max(max_seen,get_energised_count(i, up))
    max_seen = max(max_seen,get_energised_count(i, down))
max_seen
# %%
