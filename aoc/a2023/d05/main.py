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
txt = p.get_data(-1, [
    """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
])
sum_v = 0
header, *data = txt.split("\n\n")
seeds = p.get_ints(header)
min_seed = defaultdict(lambda:[float("inf")]*len(seeds))
min_seed["seed"] = seeds
for d in data:
    ln_header, *ln_data = d.splitlines()
    src, dst = ln_header.split(" map:")[0].split("-to-")
    for ln in ln_data:
        dst_r, src_r, steps = p.get_ints(ln)
        for i, s in enumerate(min_seed[src]):
            if s < src_r or s >= src_r+steps: continue
            # if min_seed[dst][i] >= dst_r+steps:continue
            min_seed[dst][i] = min(
                min_seed[dst][i],
                s-src_r+dst_r
            )
    for i, s in enumerate(min_seed[src]):
        if min_seed[dst][i] == float('inf'):
            min_seed[dst][i] = s
    # ln.split()+
    # p.get_ints(ln)

min(min_seed['location'])
#%%
puzzle.answer_a = min(min_seed['location'])
# %%
txt = p.get_data(-1, [
    """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
])

header, *data = txt.split("\n\n")
seeds = p.get_ints(header)
seeds_prv = [(st,st+lv-1) for st,lv in zip(seeds[::2],seeds[1::2])]
for d in data:
    ln_header, *ln_data = d.splitlines()
    # src, dst = ln_header.split(" map:")[0].split("-to-")
    seeds = [[(float("inf"), float("inf"))] for s in seeds_prv]
    mapped_ranges = [[s] for s in seeds_prv]
    for ln in ln_data:
        dst_r, src_r, steps = p.get_ints(ln)
        for i, (s_st, s_ed) in enumerate(seeds_prv):
            if s_ed < src_r or s_st >= src_r+steps: continue
            new_st, new_ed = max(s_st, src_r), min(s_ed, src_r+steps-1)
            mapped_ranges[i].append((new_st, new_ed))
            seeds[i].append((new_st-src_r+dst_r, new_ed-src_r+dst_r))
    
    mapped_ranges = [v for l in mapped_ranges for v in l]
    seeds = [v for l in seeds for v in l]
    # for i,s in enumerate(mapped_ranges):
    #     is_overlap = len(s) > 1
    #     s_new = seeds[i]
    for j, (st1, ed1) in enumerate(mapped_ranges):
        for k, (st2, ed2) in enumerate(mapped_ranges[j+1:], start=j+1):
            if st1 is None or st2 is None: continue
            max_st = max(st1,st2)
            min_ed = min(ed1,ed2)
            if max_st > min_ed: continue
            mapped_ranges[k] = (None, None)
            if st1 > st2:
                mapped_ranges.append((st2, max_st-1))
                seeds.append((seeds[k][0],seeds[k][0]+max_st-1 - st2))
            elif st1<st2:
                mapped_ranges.append((st1, max_st-1))
                seeds.append((seeds[j][0],seeds[j][0]+max_st-1 - st1))
            
            if ed1 > ed2:
                mapped_ranges.append((min_ed+1, ed1))
                seeds.append((seeds[j][1]-(ed1-(min_ed+1)),seeds[j][1]))
            elif ed1<ed2:
                mapped_ranges.append((min_ed+1, ed2))
                seeds.append((seeds[k][1]-(ed2-(min_ed+1)),seeds[k][1]))

            mapped_ranges[j] = (max_st, min_ed)
            st1, ed1 = mapped_ranges[j]
            seed_1_st = (seeds[j][0]-st1+max_st, seeds[j][0]-st1+min_ed)
            seed_2_st = (seeds[k][0]-st2+max_st, seeds[k][0]-st1+min_ed)
            min_st = min(seed_1_st, seed_2_st)
            seeds[j] = min_st
    
    seeds_prv = []
    for i, s in enumerate(seeds):
        if mapped_ranges[i][0] is None: continue
        if s[0] == float("inf"):
            seeds_prv.append(mapped_ranges[i])
        else: seeds_prv.append(seeds[i])

        # while is_overlap:
        #     st1, ed1 = s[0]
        #     st2, ed2 = s[1]
        #     st1_n, st2_n = s_new.pop(0)
        #     ed1_n, ed2_n = s_new.pop(0)
        #     if st1 > st2



#             # if min_seed[dst][i] >= dst_r+steps:continue
#             min_seed[dst][i] = min(
#                 min_seed[dst][i],
#                 s-src_r+dst_r
#             )
#     for i, s in enumerate(min_seed[src]):
#         if min_seed[dst][i] == float('inf'):
#             min_seed[dst][i] = s
#     # ln.split()+
#     # p.get_ints(ln)

# min(min_seed['location'])
seeds_prv
# %%
min(seeds_prv)
# %%
