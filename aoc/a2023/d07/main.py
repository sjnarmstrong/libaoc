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
"""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""","""JJJJJ 1
"""
])
sum_v =0
ranks = []
bids = []
strengths = ["A", "K", "Q", "T"] + [str(i) for i in reversed(range(10))] + ["J"]
strengths = {v:i for i,v in enumerate(strengths)}
for ln in txt.splitlines():
    cards, bid = ln.split(" ")
    bit = int(bid)
    counts = Counter(cards)
    max_counts = max((v for k,v in counts.items() if k!= "J"), default=0)
    if (max_counts + counts.get("J",0))>=5:
        rank = 0, *[strengths[c] for c in cards] #*counts.most_common()
        print(cards, "is 5")
    elif (max_counts + counts.get("J",0))==4:
        rank = 1, *[strengths[c] for c in cards] # *counts.most_common()
        print(cards, "is 4")
    elif (max_counts + counts.get("J",0))>=3 and ((len(counts) == 2) or (len(counts) == 3 and "J" in counts)):
        rank = 2, *[strengths[c] for c in cards] # *counts.most_common()
        print(cards, "is 3 and 2")
    elif (max_counts + counts.get("J",0))>=3:
        rank = 3,*[strengths[c] for c in cards] # *counts.most_common()
        print(cards, "is 3")
    elif (max_counts + counts.get("J",0))>=2 and ((len(counts) == 3) or (len(counts) == 4 and "J" in counts) or (counts["J"]>=2)):
        rank = 4, *[strengths[c] for c in cards] # *counts.most_common()
        print(cards, "is 2 and 2")
    elif (max_counts + counts.get("J",0))>=2:
        rank =5, *[strengths[c] for c in cards] # *counts.most_common()
        print(cards, "is 2")
    else:
        rank = 6, *[strengths[c] for c in cards] #
        print(cards, "is None")
    ranks.append((*rank, bit))
    # bids.append(bit)
score = 0
for i, (r, *_, b) in enumerate(reversed(sorted(ranks)), start=1):
    score += i*b

score
# min(min_seed['location'])
#%%
puzzle.answer_a = score
# %%
puzzle.answer_b = score
# %%
