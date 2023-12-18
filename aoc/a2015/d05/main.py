#%%
import sys
sys.path.append("../../..")
from aocd.utils import http

http.pool_manager.connection_pool_kw["cert_reqs"] = 'CERT_NONE'

from libaoc import parse as p, util, vec
from itertools import combinations
import math
import re
#%%
puzzle = p.get_puzzle()
# %%
txt = p.get_data(-1, ["^>v<", "^v^v^v^v^v"])

def is_nice(val: str):
    if not re.search("(?P<w>\w)(?P=w)", val): return False
    if len(re.findall("[aeiou]", val))<3: return False
    for w in ["ab", "cd", "pq", "xy"]:
        if w in val: return False
    return True

cnt = 0
for ln in txt.splitlines():
    cnt += is_nice(ln)
# %%
puzzle.answer_a = cnt
# %%
txt = p.get_data(-1, ["^>v<", "^v^v^v^v^v"])

def is_nice(val: str):
    if not re.search("(?P<w>\w\w)\w*(?P=w)", val): return False
    if not re.search("(?P<w>\w)\w(?P=w)", val): return False
    return True

cnt = 0
for ln in txt.splitlines():
    cnt += is_nice(ln)
# %%
puzzle.answer_b = cnt

# %%
