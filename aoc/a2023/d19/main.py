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

txt = p.get_data(-1, [r"""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""",r"""px{a<2000:A,m>2000:A,rz}
in{s<1000:px,qqz}
qqz{s>2000:px,m<1000:A,R}
rz{x>100:R,A}

{x=787,m=2655,a=1222,s=2876}"""])

# s<=999: px
#     a<=1999: A
#     a>1999 and m>2000: A
#     a>1999 and m<=2000: rz
#         x<=100: A
# s>999: qqz
#     s>2000:
#         a<=1999: A
#         a>1999 and m>2000: A
#         a>1999 and m<=2000: rz
#             x<=100: A
#     s<=2000 and m<1000: A

instructions, parts = txt.split("\n\n")
instr = {}
for i in instructions.splitlines():
    key, rules = i.split("{")
    rules = rules.split("}")[0]
    rule_seq = []
    for r in rules.split(",")[:-1]:
        rv, dst = r.split(":")
        rule_seq.append((rv,dst))
    rule_seq.append(("True",rules.split(",")[-1]))
    instr[key] = rule_seq

def get_result(val, args):
    for rv, dst in instr[val]:
        # print(rv, dst)
        if eval(rv,args): return dst

sum_v = 0
for part in parts.splitlines():
    part = part[1:-1].split(",")
    kwargs = {
        (arg_parts:=arg.split("="))[0]:int(arg_parts[1]) for arg in part
    }
    kwarg_values = sum(kwargs.values())
    pk = "in"
    while pk not in ["A", "R"]: 
        pk = get_result(pk, kwargs)
        # print(pk)
    if pk == "A": sum_v += kwarg_values
sum_v
# %%
from dataclasses import dataclass

@dataclass
class CondNode:
    name: str
    lte: int = 4000
    gt: int = 0
    def copy(self):
        return CondNode(
            self.name,
            self.lte,
            self.gt
        )
    def __lt__(self, other):
        self.lte = min(self.lte, other-1)
        return False
    def __gt__(self, other):
        self.gt = max(self.gt, other)
        return False
    def size(self):
        return max(self.lte - self.gt, 0)

def get_inverse(current_node_args, prev_node_args):
    diff_args = {}
    for k, v in current_node_args.items():
        v2 = prev_node_args[k]
        if v.gt != v2.gt:
            nv = v2.copy()
            nv.lte = v.gt
            diff_args[k] = nv
        elif v.lte != v2.lte:
            nv = v2.copy()
            nv.gt = v.lte
            diff_args[k] = nv
        if v.gt == v2.gt and v.lte == v2.lte:
            diff_args[k] = v.copy()
    return diff_args

def dfs(rk: str, node_args=None):
    if node_args is None:
        node_args = {k: CondNode(k) for k in "xmas"}
    accept_possibilities = []
    prev_node_args = node_args
    current_node_args = {k: v.copy() for k,v in prev_node_args.items()}
    for rv, dst in instr[rk]:
        eval(rv,current_node_args)
        current_node_args = {k: current_node_args[k] for k in "xmas"}
        if dst not in ["A","R"]:
            accept_possibilities.extend(dfs(dst, current_node_args))
        if dst == 'A':
            accept_possibilities.append(current_node_args)
        # prev_node_args_hold = current_node_args
        current_node_args = get_inverse(current_node_args, prev_node_args)
        prev_node_args = {k: v.copy() for k,v in current_node_args.items()}
        # prev_node_args = prev_node_args_hold
    return accept_possibilities
possibilities = dfs("in")

sum_v = 0
for poss in possibilities:
    red = 1
    for v in poss.values():
        red *= v.size()
    sum_v += red
sum_v
# %%
def get_str(nodes: dict[str,CondNode]):
    items = []
    for k in 'samx':
        v = nodes[k]
        if v.lte != 4000: items.append(f"{k}<={v.lte}")
        if v.gt != 0: items.append(f"{k}>{v.gt}")
    return ",".join(items)