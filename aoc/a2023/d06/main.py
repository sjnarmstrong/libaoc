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

txt = p.get_data(-1, [
"""Time:      7  15   30
Distance:  9  40  200
"""
])
time = p.get_ints(txt.splitlines()[0])
dist = p.get_ints(txt.splitlines()[1])

def calc(time_remaining: int, dist_remaining: int):
    possibilities = []
    for hold_time in range(1,time_remaining):
        distance_achieved = hold_time*(time_remaining-hold_time)
        if distance_achieved > dist_remaining:
            possibilities.append(hold_time)
    return possibilities

math.prod(list(map(lambda v: len(calc(*v)), zip(time, dist))))
# min(min_seed['location'])
#%%
puzzle.answer_a = 170000
# %%
txt = p.get_data(-1, [
"""Time:      7  15   30
Distance:  9  40  200
"""
])
time = p.get_ints(txt.splitlines()[0].replace(" ",""))
dist = p.get_ints(txt.splitlines()[1].replace(" ",""))

def calc(time_remaining: int, dist_remaining: int):
    possibilities = []
    for hold_time in range(1,time_remaining):
        distance_achieved = hold_time*(time_remaining-hold_time)
        if distance_achieved > dist_remaining:
            possibilities.append(hold_time)
    return possibilities

math.prod(list(map(lambda v: len(calc(*v)), zip(time, dist))))
# %%
import cpmpy as cp
from cpmpy.solvers.ortools import OrtSolutionPrinter
txt = p.get_data(-1, [
"""Time:      7  15   30
Distance:  9  40  200
"""
])
time = p.get_ints(txt.splitlines()[0])
dist = p.get_ints(txt.splitlines()[1])

res = 1
for t,d in zip(time,dist):
    x = cp.intvar(1,t, name="x")
    m = cp.Model((t-x)*x > d)
    solutions = []
    def collect():
        solutions.append(x.value())
    cnt = m.solveAll(display=collect)
    res *=cnt
    # s = cp.SolverLookup.get("ortools", m) # faster on a solver interface directly

    # while s.solve():
    #     print(x.value())
    #     # block this solution from being valid
    #     s += ~all(x == x.value())
res
# %%
