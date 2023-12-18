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
# %%
#%%
puzzle = p.get_puzzle()
# %%
txt = p.get_data(-1, [
    """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""","""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
])
#%%
s = 0
for ln in txt.splitlines():
    ds = p.get_ints(ln, keep_str=True)
    digets = int(''.join([ds[0][0], ds[-1][-1]]))
    print(digets)
    s+=digets



#%%
puzzle.answer_a =s
#%%
s = 0
import re as re

for ln in txt.splitlines():
    ln = ln.lower()
    matches = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))", ln)
    first_match, last_match = matches[0], matches[-1]
    ln = ''.join([first_match, last_match])
    ln = ln.replace("one","1")
    ln = ln.replace("two","2")
    ln = ln.replace("three","3")
    ln = ln.replace("four","4")
    ln = ln.replace("five","5")
    ln = ln.replace("six","6")
    ln = ln.replace("seven","7")
    ln = ln.replace("eight","8")
    ln = ln.replace("nine","9")
    ln = ln.replace("zero","0")
    # ds = ''.join(p.get_ints(ln, keep_str=True))
    digets = int(ln)
    print(digets)
    s+=digets

#%%
#%%
puzzle.answer_b = s
# %%
team-channel-alerts/WATCHLIST2023-11-25.csv