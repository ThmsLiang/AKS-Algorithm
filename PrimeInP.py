from sympy import symbols, gcd, primerange, isprime, sqrt, log, floor
from sympy.polys.polytools import Poly
from sympy.ntheory import isprime, totient


def aks(n):
    # Preliminary checks for small values of n, even numbers, etc.
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Step 1: Check if n is a perfect power: n = a^b
    a = 2
    while a * a <= n:
        b = 2
        while a**b <= n:
            if a**b == n:
                return False
            b += 1
        a += 1

    # Step 2: Find the smallest r such that ordr(n) > log2(n)^2
    max_k = int(log(n, 2) ** 2)
    r = 2
    while True:
        k = 1
        while k <= max_k and pow(n, k, r) != 1:
            k += 1
        if k > max_k:
            break
        r += 1

    # Step 3: Check if 1 < gcd(a,n) < n for a in {2,3,...,r}
    for a in range(2, r + 1):
        if 1 < gcd(a, n) < n:
            return False

    # Step 4: If n <= r, return true.
    if n <= r:
        return True

    # Step 5: Check if (X+a)^n ≡ X^n + a (mod X^r - 1, n)
    # for a in {1, ..., √ϕ(r) log n}
    X = symbols("X")
    for a in range(1, floor(sqrt(totient(r)) * log(n, 2)) + 1):
        lhs = Poly((X + a) ** n, X).all_coeffs()
        rhs = [0] * (n - 1) + [a, 1]
        if not all((lhs[i] - rhs[i]) % n == 0 for i in range(min(len(lhs), len(rhs)))):
            return False

    return True

## Print all prime between [2, 50]
for i in range(2, 50):
    if aks(i):
        print(i)
        print()
