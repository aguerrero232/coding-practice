# %%
# function to add the numbers in the fibonacci sequence that are even
def fibaddeven(n):
    a, b, s = 0, 1, 0
    while a < n:
        if a % 2 == 0:
            s += a
        a, b = b, a + b
    return s


print(fibaddeven(4000000))
