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

txt = p.get_data(-1, [r"""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""])

world = list(map(lambda ln: list(map(int, ln)), txt.splitlines()))
width = len(world[0])
height = len(world)

@dataclass(order=True)
class PrioritizedItem:
    cost: int
    pos: complex=field(compare=False)
    last_dir: complex=field(compare=False)

to_explore = [PrioritizedItem(0,0,0)]
seen = defaultdict(lambda:defaultdict(lambda:float('inf')))
# seen = defaultdict(lambda:float('inf'))

up = -1j
down = 1j
left = -1
right = 1
directions = [up, down, left, right]
def complex_dot(c1:complex,c2:complex):
    return c1.real*c2.real + c1.imag*c2.imag
def mag(c1:complex):
    return c1.real + c1.imag

pbar = tqdm()
end = complex(width-1,height-1)
while len(to_explore):
    item = heapq.heappop(to_explore)
    prev_cost, pos, last_dir = item.cost, item.pos, item.last_dir
    if pos.imag < 0 or pos.imag >= height: continue
    if pos.real < 0 or pos.real >= width: continue
    pos_cost = world[int(pos.imag)][int(pos.real)] + prev_cost
    if seen[pos][last_dir] > pos_cost:
        seen[pos][last_dir] = pos_cost
    # if seen[pos] > pos_cost:
    #     seen[pos] = pos_cost
    else:
        continue # Dont bother exploring node

    if pos == end:
        break

    pbar.update()
    for d in directions:
        dot_product = complex_dot(last_dir, d)
        if dot_product < 0: continue # Going backwards
        # Store the new length
        next_dir = d*dot_product+d
        if mag(next_dir) > 3: continue
        new_pos = pos+d
        heapq.heappush(to_explore, PrioritizedItem(pos_cost,new_pos,next_dir))

min(seen[end].values())-world[0][0]
# %%
def get_smallest_dir(pos:complex):
    return min((v,k) for k,v in seen[pos].items())[1]
def get_path():
    start = complex(width-1,height-1)
    nodes = [start]
    d = get_smallest_dir(nodes[-1])
    abs_dir = d/mag(d)
    nodes_dir = [abs_dir]
    while nodes[-1] != 0:
        d = get_smallest_dir(nodes[-1])
        abs_dir = d/mag(d)
        while mag(d) != 0:
            nodes.append(nodes[-1]-abs_dir)
            nodes_dir.append(abs_dir)
            test_d = get_smallest_dir(nodes[-1])
            d -= abs_dir
            assert mag(d) == 0 or test_d == d
    return nodes, nodes_dir
get_path()
#%%
from collections import defaultdict
from functools import lru_cache
from itertools import repeat, combinations, chain
from tqdm.auto import tqdm
from dataclasses import dataclass, field
import heapq

txt = p.get_data(-1, [r"""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""",r"""111111111111
999999999991
999999999991
999999999991
999999999991"""])

world = list(map(lambda ln: list(map(int, ln)), txt.splitlines()))
width = len(world[0])
height = len(world)

@dataclass(order=True)
class PrioritizedItem:
    cost: int
    pos: complex=field(compare=False)
    last_dir: complex=field(compare=False)

to_explore = [PrioritizedItem(0,0,0)]
seen = defaultdict(lambda:defaultdict(lambda:float('inf')))
# seen = defaultdict(lambda:float('inf'))

up = -1j
down = 1j
left = -1
right = 1
directions = [up, down, left, right]
def complex_dot(c1:complex,c2:complex):
    return c1.real*c2.real + c1.imag*c2.imag
def mag(c1:complex):
    return c1.real + c1.imag

pbar = tqdm()
end = complex(width-1,height-1)
while len(to_explore):
    item = heapq.heappop(to_explore)
    prev_cost, pos, last_dir = item.cost, item.pos, item.last_dir
    if pos.imag < 0 or pos.imag >= height: continue
    if pos.real < 0 or pos.real >= width: continue
    pos_cost = world[int(pos.imag)][int(pos.real)] + prev_cost
    if seen[pos][last_dir] > pos_cost:
        seen[pos][last_dir] = pos_cost
    # if seen[pos] > pos_cost:
    #     seen[pos] = pos_cost
    else:
        continue # Dont bother exploring node

    if pos == end:
        break

    pbar.update()
    for d in directions:
        dot_product = complex_dot(last_dir, d)
        if dot_product < 0: continue # Going backwards
        # Store the new length
        next_dir = d*dot_product+d
        if abs(mag(next_dir)) > 10: continue
        if last_dir != 0 and abs(mag(next_dir)) == 1 and abs(mag(last_dir))<4: continue
        new_pos = pos+d
        if new_pos == end and mag(next_dir)<4: continue
        heapq.heappush(to_explore, PrioritizedItem(pos_cost,new_pos,next_dir))

# min(seen[end].values())-world[0][0]
min(seen[end].values())-world[0][0]
# %%
