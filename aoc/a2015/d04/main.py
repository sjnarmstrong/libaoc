#%%
from hashlib import md5

i=0
while True:
    i+=1
    h = md5(f"iwrupvqb{i}".encode())
    if h.hexdigest().startswith("000000"):
        break
i
# %%
