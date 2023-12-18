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
from itertools import repeat, combinations, chain
txt = p.get_data(-1, [
"""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
])

@lru_cache()
def count_combos(val, remaining):
    if (len(remaining) == 0) or (len(remaining) == 1 and remaining[0]==0): 
        if "#" in val: 
            # print(f"err: {val}")
            return 0
        # print(val)
        return 1
    if len(val) == 0: return 0
    if val[0] == "?":
        res = count_combos(
            "#"+val[1:],
            remaining
        )
        res += count_combos(
            "."+val[1:],
            remaining
        )
        return res
    if remaining[0] is None:
        if val[0] == ".":
            return count_combos(
                val[1:],
                remaining
            )
        return count_combos(
            val,
            remaining[1:]
        )
    
    if remaining[0] > 0:
        if val[0] == ".": return 0
        return count_combos(
            val[1:], 
            (remaining[0]-1,)+remaining[1:]
        )
    
    if remaining[0] == 0:
        if val[0] == "#": return 0
        return count_combos(val[1:], remaining[1:])

sum_cmb = 0
for ln in txt.splitlines():
    patt, counts = ln.split(" ")
    ints = list(chain.from_iterable(zip(repeat(None), p.get_ints(counts))))
    # print(patt, ints)
    cmb = count_combos("?".join([patt]*5), tuple(ints*5))
    # count_combos.clear()
    # print(cmb)
    sum_cmb += cmb
sum_cmb
# %%
