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
from collections import defaultdict
from functools import lru_cache
from itertools import repeat
txt = p.get_data(-1, [
"""..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""
])

start_node = None
lines = txt.splitlines()
nodes = [[] for _ in lines]
for j,ln in enumerate(lines):
    for i, c in enumerate(ln):
        n1, n2, n3, n4 = None, None, None, None
        if c == "|":
            if j < len(lines)-1:
                n1 = (j+1,i)
            if j > 0:
                n2 = (j-1,i)
        elif c == "-":
            if i < len(ln)-1:
                n1 = (j,i+1)
            if i > 0:
                n2 = (j,i-1)
        elif c == "L":
            if i < len(ln)-1:
                n1 = (j,i+1)
            if j > 0:
                n2 = (j-1,i)
        elif c == "J":
            if j > 0:
                n1 = (j-1,i)
            if i > 0:
                n2 = (j,i-1)
        elif c == "7":
            if j < len(lines)-1:
                n1 = (j+1,i)
            if i > 0:
                n2 = (j,i-1)
        elif c == "F":
            if j < len(lines)-1:
                n1 = (j+1,i)
            if i < len(ln)-1:
                n2 = (j,i+1)
        elif c == "S":
            start_node = (j,i)
            if j < len(lines)-1:
                n1 = (j+1,i)
            if j > 0:
                n2 = (j-1,i)
            if i < len(ln)-1:
                n3 = (j,i+1)
            if i > 0:
                n4 = (j,i-1)

        nodes[j].append((n1,n2,n3,n4))


max_len = 0
nodes_to_explore = [(start_node,0)]
seen_map = [([None] * len(lines[0])) for _ in lines]
while len(nodes_to_explore):
    node, steps = nodes_to_explore.pop(0)
    if seen_map[node[0]][node[1]] is not None: continue
    seen_map[node[0]][node[1]] = steps

    if all(n is None for n in nodes[node[0]][node[1]]):
        seen_map[node[0]][node[1]] = -1
        continue

    max_len = max(max_len,steps)
    for neighbor in nodes[node[0]][node[1]]:
        if neighbor is None: continue
        if neighbor == node: continue
        if node not in nodes[neighbor[0]][neighbor[1]]: continue
        nodes_to_explore.append((neighbor, steps+1))
max_len

#%%
print("\n".join(["".join([f"{s: >6}" if s is not None else "      "  for s in sln ]) for sln in seen_map]))
#%%
puzzle.answer_a = max_len

#%%


txt = p.get_data(0, [
"""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
])

start_node = None
lines = txt.splitlines()
nodes = [[] for _ in lines]
segments = []
for j,ln in enumerate(lines):
    for i, c in enumerate(ln):
        n1, n2, n3, n4 = None, None, None, None

        if c == "|":
            if j < len(lines)-1:
                n1 = (j+1,i)
            if j > 0:
                n2 = (j-1,i)
        elif c == "-":
            if i < len(ln)-1:
                n1 = (j,i+1)
            if i > 0:
                n2 = (j,i-1)
        elif c == "L":
            if i < len(ln)-1:
                n1 = (j,i+1)
            if j > 0:
                n2 = (j-1,i)
        elif c == "J":
            if j > 0:
                n1 = (j-1,i)
            if i > 0:
                n2 = (j,i-1)
        elif c == "7":
            if j < len(lines)-1:
                n1 = (j+1,i)
            if i > 0:
                n2 = (j,i-1)
        elif c == "F":
            if j < len(lines)-1:
                n1 = (j+1,i)
            if i < len(ln)-1:
                n2 = (j,i+1)
        elif c == "S":
            start_node = (j,i)
            if j < len(lines)-1:
                n1 = (j+1,i)
            if j > 0:
                n2 = (j-1,i)
            if i < len(ln)-1:
                n3 = (j,i+1)
            if i > 0:
                n4 = (j,i-1)
        else:
            segments.append([(i,j)])

        nodes[j].append((n1,n2,n3,n4))


def can_join(seg1, seg2):
    for s1 in seg1:
        for s2 in seg2:
            if (s1[0]-s2[0])**2 + (s1[1]-s2[1])**2 <= 2:
                return True
    return False


has_joined = True
while has_joined and len(segments) > 1:
    has_joined = False
    for i, seg1 in enumerate(segments):
        for j, seg2 in enumerate(segments[i+1:], start=i+1):
            if can_join(seg1, seg2):
                has_joined = True
                seg1.extend(segments.pop(j))
                break

segments
# %%

import cmath

txt = p.get_data(-1, [
"""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
])

# Map pipe to neighboring nodes
start_node = None
lines = txt.splitlines()
nodes = [[] for _ in lines]
segments = []
sum_map = {
    "|": ((0+1j), (0-1j)),
    "-": ((1), (-1)),
    "L": ((-1j), (1)),
    "J": ((-1j), (-1)),
    "7": ((1j), (-1)),
    "F": ((1j), (1)),
    "S": ((1), (-1), (1j), (-1j)),
}
for j,ln in enumerate(lines):
    for i, c in enumerate(ln):
        vals = sum_map.get(c,[])
        coord = complex(i,j)
        nodes[j].append(tuple([coord+v for v in vals]))
        if c == "S": start_node = coord

# find nodes part of pipe
def dfs(start_node):
    nodes_to_explore = [(start_node, set(), [])]
    while len(nodes_to_explore):
        node, seen, path = nodes_to_explore.pop(0)
        next_seen = seen.union([node])
        next_path = path + [node]
        for neighbor in nodes[int(node.imag)][int(node.real)]:
            if len(seen) > 1 and (neighbor == start_node): return next_path
            if node not in nodes[int(neighbor.imag)][int(neighbor.real)]: continue
            if neighbor in next_path: continue
            found = nodes_to_explore.insert(0, (neighbor, next_seen, next_path))

pipe_nodes = dfs(start_node)

# Label nodes to the left of pipe as -1 and nodes to the right as 1 and pipe nodes as 0 while walking through pipe from start to finish
def safe_set(loc, val):
    try:
        if inside_outside[int(loc.imag)][int(loc.real)] is None:
            inside_outside[int(loc.imag)][int(loc.real)] = val
    except IndexError: pass

inside_outside = [([None] * len(lines[0])) for _ in lines]
prev_dir = None
for node, next_node in zip(pipe_nodes, [*pipe_nodes[1:], pipe_nodes[0]]):
    new_node_dir = next_node - node
    right_dir = complex(new_node_dir.imag, - new_node_dir.real)
    right_node = right_dir + node
    left_node = node - right_dir
    inside_outside[int(node.imag)][int(node.real)] = 0
    safe_set(right_node, 1)
    safe_set(left_node, -1)
    if prev_dir is not None and prev_dir != new_node_dir:
        forward_node = node + prev_dir
        backward_node = node - new_node_dir
        diag_node = node + prev_dir - new_node_dir
        if prev_dir == right_dir:
            safe_set(forward_node, 1)
            safe_set(backward_node, 1)
            safe_set(diag_node, 1)
        else:
            safe_set(forward_node, -1)
            safe_set(backward_node, -1)
            safe_set(diag_node, -1)
    prev_dir = new_node_dir

# Keep expanding left and right nodes
def set_inside_outside(x,y, j,i):
    try:
        if inside_outside[i+y][j+x] in [1,-1]:
            inside_outside[i][j] = inside_outside[i+y][j+x]
            return True
    except IndexError: pass
    return False

print("\n".join(["".join([charmap[s] for s in sln ]) for sln in inside_outside]))
print()
is_changed = True
while is_changed:
    is_changed = False
    for j, r in enumerate(inside_outside):
        for i, c in enumerate(r):
            if c is not None or c == 0: continue
            if set_inside_outside(0,1, i, j): is_changed = True
            elif set_inside_outside(0,-1, i, j): is_changed = True
            elif set_inside_outside(1,0, i, j): is_changed = True
            elif set_inside_outside(-1,0, i, j): is_changed = True
            elif set_inside_outside(1,1, i, j): is_changed = True
            elif set_inside_outside(1,-1, i, j): is_changed = True
            elif set_inside_outside(-1,-1, i, j): is_changed = True
            elif set_inside_outside(-1,1, i, j): is_changed = True
    print("\n".join(["".join([charmap[s] for s in sln ]) for sln in inside_outside]))
    print()

#visually identify if l or r is inside (could do a check on boarder but would take too long)
# would be cool to add code that counts the total roation if it is 360 deg then R is the answer else if -360 the L is the answer
(sum(v for r in inside_outside for v in r if v ==1), 
sum(v for r in inside_outside for v in r if v ==-1))
#%%
nodes_to_explore = [start_node]
inside_outside = [([None] * len(lines[0])) for _ in lines]
seen_map = [([False] * len(lines[0])) for _ in lines]
while len(nodes_to_explore):
    node = nodes_to_explore.pop(0)
    if seen_map[int(node.real)][int(node.imag)]: continue
    seen_map[int(node.real)][int(node.imag)] = True

    for neighbor in nodes[int(node.real)][int(node.imag)]:
        if neighbor == node: continue
        if node not in nodes[int(neighbor.real)][int(neighbor.imag)]: continue
        new_node_dir = neighbor - node
        right_dir = complex(new_node_dir.imag, - new_node_dir.real)
        right_node = right_dir + neighbor
        left_node = neighbor - right_dir
        inside_outside[int(node.real)][int(node.imag)] = 0
        inside_outside[int(neighbor.real)][int(neighbor.imag)] = 0
        try:
            if inside_outside[int(right_node.real)][int(right_node.imag)] is None:
                inside_outside[int(right_node.real)][int(right_node.imag)] = 1
        except IndexError: pass
        try:
            if inside_outside[int(left_node.real)][int(left_node.imag)] is None:
                inside_outside[int(left_node.real)][int(left_node.imag)] = -1
        except IndexError: pass

        nodes_to_explore.insert(0, neighbor)
        print("\n".join(["".join([charmap[s] for s in sln ]) for sln in inside_outside]))
        print()

# %%
charmap = {1: "L", -1: "R", None: "?", 0: "."}
print("\n".join(["".join([charmap[s] for s in sln ]) for sln in inside_outside]))

# %%
