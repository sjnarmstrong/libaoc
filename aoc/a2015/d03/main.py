#%%
import sys
sys.path.append("../../..")
from aocd.utils import http

http.pool_manager.connection_pool_kw["cert_reqs"] = 'CERT_NONE'

from libaoc import parse as p, util, vec
from itertools import combinations
import math
#%%
puzzle = p.get_puzzle()
# %%
txt = p.get_data(-1, ["^>v<", "^v^v^v^v^v"])
dirs = p.Convert(vec.Vec.COMMON_MAPPINGS_2)(txt)
loc = vec.Vec(0,0)
seen = {loc}
for v in dirs:
    loc = loc + v
    seen.add(loc)
len(seen)
# %%
puzzle._submit(str(seen), 1)
# %%
puzzle.view()
# %%
txt = p.get_data(-1, ["^>v<", "^v^v^v^v^v"])
dirs = p.Convert(vec.Vec.COMMON_MAPPINGS_2)(txt)
locs = [vec.Vec(0,0),vec.Vec(0,0)]
seen = {locs[0]}
for i, v in enumerate(dirs):
    idx = i%2
    locs[idx] = locs[idx] + v
    print(locs)
    seen.add(locs[idx])
len(seen)
# %%
