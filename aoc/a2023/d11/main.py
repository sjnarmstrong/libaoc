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
from itertools import repeat, combinations
txt = p.get_data(-1, [
"""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
])
lines = txt.splitlines()
empty_rows = set(range(len(lines)))
empty_cols = set(range(len(lines[0])))

stars = []
for j,r in enumerate(lines):
    for i,c in enumerate(r):
        if c == "#":
            stars.append((j,i))
            if j in empty_rows: empty_rows.remove(j)
            if i in empty_cols: empty_cols.remove(i)

dist_sum = 0
for (s1j,s1i),(s2j,s2i) in combinations(stars,2):
    start_j = min(s1j, s2j)
    start_i = min(s1i, s2i)
    end_j = max(s1j, s2j)
    end_i = max(s1i, s2i)
    overlap_j = len(empty_rows.intersection(range(start_j,end_j+1)))
    overlap_i = len(empty_cols.intersection(range(start_i,end_i+1)))
    dist_pair = end_j-start_j + end_i-start_i + 1000000*(overlap_i+overlap_j) - (overlap_i+overlap_j)
    print((s1j,s1i),(s2j,s2i),dist_pair)
    dist_sum += dist_pair

dist_sum
#%%
#%%
puzzle.answer_b = dist_sum

#%%
