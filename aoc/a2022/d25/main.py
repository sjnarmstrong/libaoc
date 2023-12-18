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
from tqdm.auto import tqdm
from dataclasses import dataclass, field
import heapq

txt = p.get_data(-1, [r"""1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""])
val = 0
for ln in txt.splitlines():
    nr = int(ln.replace("=", "3").replace("-", "4"), 5)
    for i, strv in enumerate(reversed(ln), start=1):
        if strv in ["-", "="]:
            nr -= 5**i
    val += nr

i = 0
rem = val
bits = []
while rem>0:
    strv = str(rem%5).replace("3", "=").replace("4", "-")
    bits.insert(0,strv)
    rem = rem // 5
    rem += 1 if strv in ["-", "="] else 0
"".join(bits)
# %%
