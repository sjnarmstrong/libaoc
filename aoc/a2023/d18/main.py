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
from tqdm.auto import tqdm
from dataclasses import dataclass, field
import heapq

txt = p.get_data(-1, [r"""R 6 (\#70c710)
D 5 (\#0dc571)
L 2 (\#5713f0)
D 2 (\#d2c081)
R 2 (\#59c680)
D 2 (\#411b91)
L 5 (\#8ceee2)
U 2 (\#caa173)
L 1 (\#1b58a2)
U 2 (\#caa171)
R 2 (\#7807d2)
U 3 (\#a77fa3)
L 2 (\#015232)
U 2 (\#7a21e3)"""])

def print_trench():
    for j in range(min_y, max_y+1):
        ln = []
        for i in range(min_x, max_x+1):
            ln.append("#" if complex(i,j) in trench else ".")
        print("".join(ln))

trench = {0}
pos = 0
up = -1j
down = 1j
left = -1
right = 1
d_lookup = {
    "U" :up,
    "D" :down,
    "L" :left,
    "R" :right
}
d_lookup = [right, down, left, up]

for ln in tqdm(txt.splitlines()):
    # d, dist, color = ln.split(" ")
    d, dist, color = ln.split(" ")
    dist = int(color[2:-2],16)
    d = int(color[-2],16)
    d=d_lookup[d]
    for _ in range(int(dist)):
        pos+=d
        trench.add(pos)

print_trench()
print()
min_x = int(min(v.real for v in trench))
max_x = int(max(v.real for v in trench))
min_y = int(min(v.imag for v in trench))
max_y = int(max(v.imag for v in trench))

trench_filled = set(trench)
for j in tqdm(range(min_y, max_y+1)):
    inside = False
    last_dir = None
    for i in range(min_x, max_x+1):
        v = complex(i,j)
        if complex(i,j) in trench:
            if last_dir is None:
                if v + up in trench:
                    last_dir = up
                else:
                    last_dir = down
                inside = not inside
            else:
                if v+right not in trench:
                    if v+last_dir in trench:
                        inside = not inside
                    last_dir = None
        else:
            last_dir = None
        if inside: trench_filled.add(complex(i,j))
trench = trench_filled
print_trench()
len(trench)
# %%
def print_trench():
    for j in range(min_y, max_y):
        ln = []
        for i in range(min_x, max_x):
            ln.append("#" if complex(i,j) in trench else ".")
        print("".join(ln))
# %%
