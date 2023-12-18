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
txt = p.get_data(-1, ["""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""])

def get_hash(txt):
    sum_v = 0
    for c in txt:
        sum_v += ord(c)
        sum_v *= 17
        sum_v %= 256
    return sum_v

sum(map(get_hash, txt.split(",")))
# %%

def print_boxes():
    for box_x, box in enumerate(boxes):
        if len(box) == 0: continue
        row = " ".join(f"[{k} {v}]" for k,v in box.items())
        print(f"Box {box_x}: {row}")
    print()

from collections import OrderedDict
txt = p.get_data(-1, ["""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""])
boxes = [OrderedDict() for _ in range(256)]
patt = re.compile(r"(\w*)([=-])(\d?)")
for chars in txt.split(","):
    (lbl, op, lense_size), = patt.findall(chars)
    box_i = get_hash(lbl)
    if op == "-":
        if lbl in boxes[box_i]:
            del boxes[box_i][lbl]
    else:
        boxes[box_i][lbl] = int(lense_size)
    print(chars, box_i)
    print_boxes()

sum_v = 0
for box_x, box in enumerate(boxes):
    for i, (lbl, lense_size) in enumerate(box.items()):
        sum_v += (box_x+1)*(i+1)*(lense_size)
        print(box_x, i, lbl, lense_size, (box_x+1)*(i+1)*(lense_size))
sum_v
# %%
