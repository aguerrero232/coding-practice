# %%

import numpy as np

# %%

arr = list(np.random.randint(0, 10, 15))
s = set(arr)
m = {k: arr.count(k) for k in s}


print(arr)
print(s)
print(m)

revm = {}
for k in m:
    revm[m[k]] = [x for x in m if m[x] == m[k]]
print(revm)

# %%

sorted_revm = sorted(revm.items(), key=lambda x: x[0])
strm = [str(x) for x in sorted_revm[1][1]]
strm.sort()
print(" ".join(strm))

# %%
