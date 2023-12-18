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
"""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
])

def get_differences(d):
    # if len(d)==1: 
    #     return [d[0], d[0]]

    diffs = [i - j for i,j in zip(d[1:], d)]
    # if len(diffs) == 0: return [float("nan")]
    if all(d == 0 for d in diffs): 
        return diffs + [0]
    diffs = diffs + [diffs[-1]+get_differences(diffs)[-1]]
    print(diffs)
    return diffs

sum_v = 0
data = p.get_ints(txt, per_ln=True)
for d in data:
    print("==========")
    print(d)
    diff = get_differences(d)[-1]
    if not diff == float("nan"):
        s = d[-1] + diff
    print(s)
    sum_v += s

#%%
puzzle.answer_a = sum_v

#%%

# %%
puzzle.answer_b = 8245452805243
# %%


from collections import defaultdict
from functools import lru_cache
from itertools import repeat
txt = p.get_data(-1, [
"""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
])

def get_differences(d):
    # if len(d)==1: 
    #     return [d[0], d[0]]

    diffs = [i - j for i,j in zip(d[1:], d)]
    # if len(diffs) == 0: return [float("nan")]
    if all(d == 0 for d in diffs): 
        return [0]+diffs
    diffs = [diffs[0]-get_differences(diffs)[0]] + diffs
    print(diffs)
    return diffs

sum_v = 0
data = p.get_ints(txt, per_ln=True)
for d in data:
    print("==========")
    print(d)
    diff = get_differences(d)[0]
    if not diff == float("nan"):
        s = d[0] - diff
    print(s)
    sum_v += s

#%%
puzzle.answer_b = sum_v
# %%
