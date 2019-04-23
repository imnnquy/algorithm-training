# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=12822
# import sys

import math


def calc_result(p, q, r, s, t, u, x):

    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * math.pow(x, 2) + u


def solution():
    while True:
        try:
            p, q, r, s, t, u= map(int, input().strip().split())
            lo, hi = 0, 1
            if calc_result(p, q, r, s, t, u, lo) == 0:
                print(lo)
                continue
            if calc_result(p, q, r, s, t, u, hi) == 0:
                print(hi)
                continue

            for i in range(1000000):
                x = (lo + hi) / 2
                result = calc_result(p, q, r, s, t, u, x)

                if result == 0:
                    print(x)
                    break
                if result > 0:
                    lo = x
                if result < 0:
                    hi = x

        except Exception as e:
            break


solution()

