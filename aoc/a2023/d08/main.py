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
p.getint


#%%
puzzle.answer_a = count

#%%

# %%
puzzle.answer_b = 8245452805243
# %%
