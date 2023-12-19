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
            ln.append(("#" if trench[j][i][1] else "+") if i in trench.get(j,[]) else ".")
        print("".join(ln))

trench = defaultdict(dict)
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
data = txt.splitlines()
for ln in reversed(data):
    d, dist, color = ln.split(" ")
    d = int(color[-2],16)
    prev_d=d_lookup[d]
    if d in [up, down]: break

# def get_next_d(start):
#     for ln in chain(data[start+1:],data):
#         d, _, _ = ln.split(" ")
#         prev_d=d_lookup[d]
#         if d in [up, down]: return prev_d
def get_next_d(start):
    for ln in chain(data[start+1:],data):
        d, _, color = ln.split(" ")
        d = int(color[-2],16)
        return d_lookup[d]


for i, ln in enumerate(tqdm(txt.splitlines())):
    # d, dist, color = ln.split(" ")
    d, dist, color = ln.split(" ")
    dist = int(color[2:-2],16)
    d = int(color[-2],16)
    d=d_lookup[d]
    dist = int(dist)
    if d in [up,down]:
        for _ in range(dist):
            pos+=d
            trench[int(pos.imag)][int(pos.real)] = (1,True)
        prev_d = d
    else:
        if d == left:
            pos+=dist*d
            trench[int(pos.imag)][int(pos.real)] = (dist,get_next_d(i)==-prev_d)
        else:
            pos+=d
            trench[int(pos.imag)][int(pos.real)] = (dist,get_next_d(i)==-prev_d)
            pos+=(dist-1)*d


# min_y = int(min(v for v in trench.keys()))
# max_y = int(max(v for v in trench.keys()))
# min_x = int(min(x for v in trench.values() for x in v.keys()))
# max_x = int(max(x for v in trench.values() for x in v.keys()))
# print_trench()
# print()

# trench_filled = set(trench)
# for j in tqdm(range(min_y, max_y+1)):
#     inside = False
#     last_dir = None
#     for i in range(min_x, max_x+1):
#         v = complex(i,j)
#         if complex(i,j) in trench:
#             if last_dir is None:
#                 if v + up in trench:
#                     last_dir = up
#                 else:
#                     last_dir = down
#                 inside = not inside
#             else:
#                 if v+right not in trench:
#                     if v+last_dir in trench:
#                         inside = not inside
#                     last_dir = None
#         else:
#             last_dir = None
#         if inside: trench_filled.add(complex(i,j))
# trench = trench_filled
# print_trench()
# len(trench)

t2 = set()
sum_v = 0
for j, row in tqdm(trench.items()):
    inside = False
    last_i = None, None
    for i in sorted(row.keys()):
        dist, should_swap = row[i]
        sum_v += dist
        # for x in range(dist):
        #     nv = complex(i+x,j)
        #     if nv in t2: print(nv, "is already in when processing", j,i,dist,should_swap)
        #     t2.add(nv)
        if inside:
            sum_v += i - last_i[0] - last_i[1]
            # for x in range(last_i[1], i - last_i[0]):
            #     nv = complex(i-x,j)
            #     if nv in t2: print(nv, "is already in2", j,i,dist,should_swap)
            #     t2.add(nv)
        
        last_i = i, dist
        if should_swap: 
            inside = not inside
            


# def print_trench():
#     min_x = int(min(v.real for v in t2))
#     max_x = int(max(v.real for v in t2))
#     min_y = int(min(v.imag for v in t2))
#     max_y = int(max(v.imag for v in t2))
#     for j in range(min_y, max_y+1):
#         ln = []
#         for i in range(min_x, max_x+1):
#             ln.append("#" if complex(i,j) in t2 else ".")
#         print("".join(ln))
# print_trench()
sum_v
# %%
txt = p.get_data(1, [r"""R 6 (\#70c710)
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
U 2 (\#7a21e3)""",r"""R 2 (\#70c710)
D 1 (\#70c710)
R 1 (\#70c710)
U 1 (\#70c710)
R 3 (\#70c710)
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
# d_lookup = [right, down, left, up]

sum_v = 0

for i, ln in enumerate(tqdm(txt.splitlines())):
    d, dist, color = ln.split(" ")
    # dist = int(color[2:-2],16)
    # d = int(color[-2],16)
    d=d_lookup[d]
    dist = int(dist)
    delta = dist*d
    if delta.imag > 0:
        diff = delta.imag*pos.real - abs(delta.imag)
    else:
        diff = delta.imag*pos.real + abs(delta.imag)
    sum_v += diff
    # sum_v += dist
    if d in [left,right]:
        sum_v += dist
        # print(f"{diff}\t{dist}\t{delta}")
    # else:
    #     print(f"{diff}\t{0}\t{delta}")
    pos += delta
sum_v
# %%

txt = p.get_data(1, [r"""R 6 (\#70c710)
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
U 2 (\#7a21e3)""",r"""R 2 (\#70c710)
D 1 (\#70c710)
R 1 (\#70c710)
U 1 (\#70c710)
R 3 (\#70c710)
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
# d_lookup = [right, down, left, up]

sum_v = 0

for i, ln in enumerate(tqdm(txt.splitlines())):
    d, dist, color = ln.split(" ")
    # dist = int(color[2:-2],16)
    # d = int(color[-2],16)
    d=d_lookup[d]
    dist = int(dist)
    delta = dist*d
    diff = delta.imag*pos.real
    if diff >= 0:
        diff = (abs(delta.imag)+1)*(abs(pos.real)+1)
    else:
        diff = -(abs(delta.imag))*(abs(pos.real))
    sum_v += diff
    # sum_v += dist
    # if d in [left,right]:
    #     sum_v += dist
        # print(f"{diff}\t{dist}\t{delta}")
    # else:
    #     print(f"{diff}\t{0}\t{delta}")
    pos += delta
sum_v
# %%
