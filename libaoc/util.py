def cum_sum(values):
    s = 0
    out = [0]*len(values)
    for i,v in enumerate(values):
        s+=v
        out[i] = s
    return out