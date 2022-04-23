# %%
import time
from itertools import combinations


def lcm(num1, num2):
    if num1 > num2:
        num = num1
    else:
        num = num2
    while(True):
        if((num % num1 == 0) and (num % num2 == 0)):
            lcm = num
            break
        num += 1
    return lcm


# Naive solution
def calc_On(n, d_nums):
    return sum([x for x in range(1, n) if 0 in [x % y for y in d_nums]])

# Optimized solution


def calc_O1(n, d_nums, lcms):
    # d = numbers to find divisibility from range, lcm = least common multiple of numbers d, n = number range
    # Sum = for each d: d*(n/d)*(1+(n/d)) - for each lcm: lcm*(n/lcm)*(1+(n/lcm)) /2
    n, val = n-1, 0  # number range 0 - n-1, n total numbers
    for d in d_nums:
        val += d * (n // d) * ((n // d) + 1)
    for lcm in lcms:
        val -= lcm * (n // lcm) * ((n // lcm) + 1)
    return val / 2


n = 1000
d_nums = [3, 5]
lcms = [lcm(x, y) for x, y in combinations(d_nums, 2)]

# convert d_nums to string for printing
d_nums_str = ', '.join([str(x) for x in d_nums])


print(f"Finding the sum of all the multiples of {d_nums_str} below {n}")
starton = time.time()
son = calc_On(n, d_nums)
endon = time.time()
starto1 = time.time()
so1 = calc_O1(n, d_nums, lcms)
endo1 = time.time()

print(f"time to sum O(n): {endon - starton}")
print(f"sum O(n): {son}")

print(f"time to sum O(1): {endo1 - starto1}")
print(f"sum O(1): {so1}")

# %%
