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
txt = p.get_data(0, ["""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
])

rocks = []
barriers = set()
height = len(txt.splitlines())
width = len(txt.splitlines()[0])
for j,ln in enumerate(txt.splitlines()):
    for i, c in enumerate(ln):
        if c == "#":
            barriers.add(complex(i,j))
        if c == "O":
            rocks.append(complex(i,j))

def move_rocks( md):
    global rocks
    moved = True
    while moved:
        moved = False
        for i, r in enumerate(rocks):
            new_r: complex = r + md
            if new_r.imag < 0: continue
            if new_r.real < 0: continue
            if new_r.imag >= height: continue
            if new_r.real >= width: continue
            if new_r in barriers: continue
            if new_r in rocks: continue
            moved = True
            rocks[i] = new_r
            # print(new_r)
move_rocks(-1j)
sum_v = 0
for rock in rocks:
    sum_v += height - rock.imag
    print(rock)
sum_v
# %%
from tqdm.auto import tqdm
txt = p.get_data(-1, ["""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
])

rocks = []
barriers = set()
height = len(txt.splitlines())
width = len(txt.splitlines()[0])
for j,ln in enumerate(txt.splitlines()):
    for i, c in enumerate(ln):
        if c == "#":
            barriers.add(complex(i,j))
        if c == "O":
            rocks.append(complex(i,j))

def print_rocks(rocks):
    print("\n".join([''.join(["O" if complex(i,j) in rocks else "." for i in range(width)]) for j in range(height)]))

# print_rocks(rocks)
cache = {}
i = 0
end = 1000000000
pbar = tqdm(total=end)
while i < end:
    rocks = move_rocks(rocks, -1j)
    # print()
    # print_rocks(rocks)
    rocks = move_rocks(rocks,-1)
    # print()
    # print_rocks(rocks)
    rocks = move_rocks(rocks,1j)
    # print()
    # print_rocks(rocks)
    rocks = move_rocks(rocks,1)
    # print()
    # print_rocks(rocks)
    # print("#####")
    # for r in rocks:
    #     print(r)
    rock_lookup = tuple(rocks)
    if rock_lookup in cache:
        print(i, cache[rock_lookup])
        diff = i-cache[rock_lookup]
        jump = int(diff*((end-i)//diff))
        if jump > 0:
            i += jump+1
            pbar.update(jump+1)
            continue
    cache[rock_lookup] = i
    i+=1
    pbar.update()
sum_v = 0
for rock in rocks:
    sum_v += height - rock.imag
sum_v
# %%
from tqdm.auto import tqdm
txt = p.get_data(0, ["""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
])

rocks = []
barriers = set()
height = len(txt.splitlines())
for j,ln in enumerate(txt.splitlines()):
    width = len(ln)
    for i, c in enumerate(ln):
        if c == "#":
            barriers.add(complex(i,j))
        if c == "O":
            rocks.append(complex(i,j))


def complex_dot(c1:complex,c2:complex):
    return c1.real*c2.real + c1.imag*c2.imag

@lru_cache()
def get_barriers_per_col(md: complex):
    barriers_per_col = [[] for i in range(height if md.real == 0 else width)]
    for b in barriers:
        col = b.real if md.real == 0 else b.imag
        dist = complex_dot(b, md)
        barriers_per_col[int(col)].append(dist)

    start = complex_dot(complex(-1,-1), md)
    end = complex_dot(complex(width,height), md)
    for c in barriers_per_col:
        c.extend([start, end])
    barriers_per_col = [sorted(c, reverse=True) for c in barriers_per_col]
    return barriers_per_col

def move_rocks(rocks: list[complex], md: complex):
    rocks_per_col = [[] for i in range(height if md.real == 0 else width)]
    for rock in rocks:
        col = rock.real if md.real == 0 else rock.imag
        dist = complex_dot(rock, md)
        rocks_per_col[int(col)].append(dist)

    barriers_per_col = get_barriers_per_col(md)
    new_rocks = []
    for ci, (col, bcol) in enumerate(zip(rocks_per_col, barriers_per_col)):
        col = sorted(col, reverse=True)
        barrier_idx = 0
        i = 0
        abs_dir = abs(md.real + md.imag)
        dist = bcol[barrier_idx] - abs_dir
        while i < len(col):
            if col[i] <= bcol[barrier_idx+1]:
                barrier_idx += 1
                dist = bcol[barrier_idx] - abs_dir
            else:
                new_rocks.append(
                    complex(ci, abs(dist)) 
                    if md.real == 0 else 
                    complex(abs(dist), ci)
                )
                i+=1
                dist -= abs_dir
    return new_rocks
    
        

# for i in tqdm(range(1000000000)):
#     rocks = move_rocks(rocks, -1j)
#     rocks = move_rocks(rocks, -1)
#     rocks = move_rocks(rocks, 1)
#     rocks = move_rocks(rocks, 1j)
# # rocks = move_rocks(rocks, 1)
# # rocks = move_rocks(rocks, 1j)
# # rocks = move_rocks(rocks, -1j)
# sum_v = 0
# for rock in rocks:
#     sum_v += height - rock.imag
#     print(rock)
# sum_v
# %%
