#%% New 
import sys
sys.path.append("../../..")
from libaoc import parse as p, util

txt = p.get_data(-1, [])
values = p.Convert(
    map_vals = {"(": 1, ")": -1},
    iterate=True
)(txt)
values = util.cum_sum(values)
values[-1], values.index(-1)+1
#%% OLD
from collections import Counter

with open("./data.txt", "r") as fp:
    txt = fp.read()

counts = Counter(txt)
counts['('] - counts[')']
# %%
floor = 0
for i, c in enumerate(txt):
    floor += 1 if c == "(" else -1
    if floor == -1: break
i+1
# %%
