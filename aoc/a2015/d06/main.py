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
#%%
puzzle = p.get_puzzle()
# %%
txt = p.get_data(-1, ["^>v<", "^v^v^v^v^v"])
# %%
overall_map = np.zeros((1000, 1000), dtype=np.bool_)
for ln in txt.splitlines():
    x1,y1, x2, y2 = p.get_ints(ln)
    x2 +=1
    y2 +=1
    if ln.startswith("turn on"):
        overall_map[x1: x2, y1:y2] = True
    if ln.startswith("turn off"):
        overall_map[x1: x2, y1:y2] = False
    if ln.startswith("toggle"):
        overall_map[x1: x2, y1:y2] = ~overall_map[x1: x2, y1:y2]
# %%
puzzle.answer_a = overall_map.sum()
# %%
# txt = "turn on 0,0 through 0,0\ntoggle 0,0 through 999,999"
overall_map = np.zeros((1000, 1000), dtype=np.int64)
for ln in txt.splitlines():
    x1,y1, x2, y2 = p.get_ints(ln)
    x2 +=1
    y2 +=1
    if ln.startswith("turn on"):
        overall_map[x1: x2, y1:y2] += 1
    if ln.startswith("turn off"):
        overall_map[x1: x2, y1:y2] = np.clip(overall_map[x1: x2, y1:y2]-1,0, None)
    if ln.startswith("toggle"):
        overall_map[x1: x2, y1:y2] += 2
# %%
puzzle.answer_b = overall_map.sum()
# %%
