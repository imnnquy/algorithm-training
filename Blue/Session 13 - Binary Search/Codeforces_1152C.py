# Problem from Codeforces
# http://codeforces.com/problemset/problem/1152/C
from math import sqrt

INF = 1e18


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def solution():
    atmp, btmp = map(int, input().strip().split())
    a = max(atmp, btmp)
    b = min(atmp, btmp)
    k = 0

    delta = a - b
    min_lcm = INF

    if delta == 0:
        print(0)
        exit(0)

    range_gcd = int(sqrt(delta)) + 1
    for i in range(1, range_gcd):
        if delta % i == 0:
            k, min_lcm = getk(a, b, i, k, min_lcm)
            k, min_lcm = getk(a, b, delta / i, k, min_lcm)

    print('{0:.0f}'.format(k))


def getk(a, b, i, k, min_lcm):
    current_k = 0
    if b % i > 0:
        current_k = ((b // i) + 1) * i - b
    lcm = (a + current_k) * (b + current_k) / i
    if lcm < min_lcm:
        min_lcm = lcm
        k = current_k
    return k, min_lcm


solution()
