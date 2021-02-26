import math


def ncr(n, r):
    if r > n:
        return 0
    elif r == n:
        return 1
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
