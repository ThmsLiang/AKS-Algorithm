import math
import array as arr
from math import gcd


def findR(n):
    maxK = math.log2(n) ** 2
    maxR = math.log2(n) ** 5
    nexR = True
    r = 1
    while nexR == True:
        r += 1
        nexR = False
        k = 0
        while k <= maxK and nexR == False:
            k = k + 1
            if fastMod(n, k, r) == 0 or fastMod(n, k, r) == 1:
                nexR = True
    return r


def fastMod(base, power, n):
    r = 1
    while power > 0:
        if power % 2 == 1:
            r = r * base % n
        base = base**2 % n
        power = power // 2
    return r


def fastPoly(base, power, r):
    x = arr.array(
        "d",
        [],
    )
    a = base[0]

    for i in range(len(base)):
        x.append(0)
    x[(0)] = 1
    n = power

    while power > 0:
        if power % 2 == 1:
            x = multi(x, base, n, r)
        base = multi(base, base, n, r)
        power = power // 2

    x[(0)] = x[(0)] - a
    x[(n % r)] = x[(n % r)] - 1
    return x


def multi(a, b, n, r):
    """Function used by fastPoly to multiply two polynomials together."""
    x = arr.array("d", [])
    for i in range(len(a) + len(b) - 1):
        x.append(0)
    for i in range(len(a)):
        for j in range(len(b)):
            x[(i + j) % r] += a[(i)] * b[(j)]
            x[(i + j) % r] = x[(i + j) % r] % n
    for i in range(r, len(x)):
        x = x[:-1]
    return x


def eulerPhi(r):
    x = 0
    for i in range(1, r + 1):
        if math.gcd(r, i) == 1:
            x += 1
    return x


def aks(n):
    """Checks if number is a power of another integer,"""
    for b in range(2, int(math.log2(n)) + 1):
        a = n ** (1 / b)
        if a - int(a) == 0:
            return "Composite"

    r = findR(n)  # step 2

    for a in range(2, min(r, n)):  # step 3
        if math.gcd(a, n) > 1:
            return "Composite"

    if n <= r:  # step 4
        return "Prime"

    x = arr.array(
        "l",
        [],
    )  # step 5
    for a in range(1, math.floor((eulerPhi(r)) ** (1 / 2) * math.log2(n))):
        x = fastPoly(arr.array("l", [a, 1]), n, r)
        if any(x):
            return "Composite"
    return "Prime"  # step 6


""" Print all prime numbers in [2, 1000]"""
for a in range(2, 1000):
    if aks(a) == "Prime":
        print(a)
        print()
