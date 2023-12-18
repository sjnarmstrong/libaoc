#%%
from collections import Counter
from itertools import combinations
with open("./data.txt", "r") as fp:
    txt = fp.read()
#%%
# txt = "2x3x4"
total_area = 0
for ln in txt.splitlines():
    l,w,h = ln.split("x")
    # ints in parser would be good
    l,w,h = int(l),int(w),int(h)
    side_areas = list(map(
        lambda x: 2*x[0]*x[1],
        combinations([l,w,h], 2)
    ))
    # print(list(combinations([l,w,h], 2)),side_areas)
    total_area += min(side_areas)//2
    total_area += sum(side_areas)
total_area
# %%
# txt = "2x3x4"
total_area = 0
for ln in txt.splitlines():
    l,w,h = ln.split("x")
    # ints in parser would be good
    l,w,h = int(l),int(w),int(h)
    side_areas = list(map(
        lambda x: 2*(x[0]+x[1]),
        combinations([l,w,h], 2)
    ))
    # print(list(combinations([l,w,h], 2)),side_areas)
    total_area += min(side_areas) + l*w*h
total_area
# %%
import sys
sys.path.append("../../..")

from libaoc import parse as p, util
from itertools import combinations
txt = p.get_data(-1, [])
values = p.Apply(
    p.Chain([
        p.extract_ints,
        p.partial(combinations, r=2),
        list,
        p.Apply(
            lambda x: x[0]*x[1]
        ),
        lambda x: min(x)+2*sum(x)
    ])
)(txt.splitlines())

sum(values)
#%% Seminew
import sys
sys.path.append("../../..")

from libaoc import parse as p, util
from itertools import combinations
import math

txt = p.get_data(-1, ["2x3x4"])
total_area = 0
for lwh in p.get_ints(txt, per_ln=True):
    side_areas = [math.prod(x) for x in combinations(lwh, 2)]
    # print(list(combinations([l,w,h], 2)),side_areas)
    total_area += min(side_areas) + 2*sum(side_areas)
total_area
# %%
