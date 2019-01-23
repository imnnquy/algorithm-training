# Problem from Codeforces
# http://codeforces.com/problemset/problem/600/B

import bisect


def solution():
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    a.sort()

    for i in range(m - 1):
        print(bisect.bisect_right(a, b[i]), end=' ')
        # print(binary_search(a, b[i], -1, n), end=' ')
    print(bisect.bisect_right(a, b[m - 1]))


solution()
