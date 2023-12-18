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
txt = p.get_data(-1, ["""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""","""##..###
.####..
#....##
..##...
#.##...
##..###
#.##.##""","""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
])

def get_ref_num(m):
    for i in range(1,len(m)):
        left, right = m[:i], m[i:]
        shortest_len = min(len(left), len(right))
        left, right = left[len(left)-shortest_len:], right[:shortest_len]
        if np.allclose(left, right[::-1]):
            return 100*i
    for i in range(1,m.shape[1]):
        left, right = m[:,:i], m[:,i:]
        shortest_len = min(left.shape[1], right.shape[1])
        left, right = left[:,left.shape[1]-shortest_len:], right[:,:shortest_len]
        if np.allclose(left, right[:,::-1]):
            return i

def get_ref_num(m):
    for i in range(1,len(m)):
        left, right = m[:i], m[i:]
        shortest_len = min(len(left), len(right))
        left, right = left[len(left)-shortest_len:], right[:shortest_len]
        if (left != right[::-1]).sum() == 1:
            return 100*i
    for i in range(1,m.shape[1]):
        left, right = m[:,:i], m[:,i:]
        shortest_len = min(left.shape[1], right.shape[1])
        left, right = left[:,left.shape[1]-shortest_len:], right[:,:shortest_len]
        if (left != right[:,::-1]).sum() == 1:
            return i

sum_v = 0
for dta in txt.split("\n\n"):
    m = np.array([
        [True if c == "#" else False for c in row] 
        for row in dta.splitlines()
    ])
    # elements = list(get_ref_num(m))
    # if len(elements) > 1:
    #     print(m)
    # sum_v += sum(get_ref_num(m),0)
    h = get_ref_num(m)
    if h is None:
        print(dta)
        print()
    else:
        sum_v += h
sum_v
# %%
