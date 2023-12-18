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
txt = p.get_data(0, [
    """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
])

map_v = txt.splitlines()
sum_v = 0
for i, r in enumerate(map_v):
    v1, v2 = r.split("|")
    v1 = p.get_ints(v1)[1:]
    v2 = p.get_ints(v2)
    powr = len(set(v1).intersection(v2))-1
    if powr < 0: continue
    sum_v += 2**powr
# print(chars)
# sum_v += sum(p.get_ints(".".join(chars)))
# sum_v

#%%
puzzle.answer_a = sum_v
# %%
from functools import lru_cache
txt = p.get_data(-1, [
    """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
])

map_v = txt.splitlines()
line_cards = {}
for i, r in enumerate(map_v):
    v1, v2 = r.split("|")
    card_no, *v1 = p.get_ints(v1)
    v2 = p.get_ints(v2)
    powr = len(set(v1).intersection(v2))
    line_cards[card_no] = list(range(card_no+1,card_no+1+powr))

# %%
to_proc = list(line_cards.keys())
copies = list(line_cards.keys())
for k in to_proc:
    to_proc.extend(line_cards[k])
    copies.extend(line_cards[k])
# %%
len(copies)
