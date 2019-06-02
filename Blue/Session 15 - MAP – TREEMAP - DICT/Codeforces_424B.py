# Problem from Codeforces
# http://codeforces.com/problemset/problem/424/B


import math


class Location:
    def __init__(self, r, k):
        self.r = r
        self.k = k

    def __lt__(self, other):
        return self.r < other.r


def solution():
    n, s = map(int, input().split())
    locations = []
    for i in range(n):
        x, y, k = map(int, input().split())
        locations.append(Location(math.sqrt(x*x + y*y), k))

    locations.sort()

    min_r = 0
    for i in range(n):
        if s >= 1000000:
            print(round(min_r, 7))
            return
        s += locations[i].k
        min_r = locations[i].r

    if s >= 1000000:
        print(round(min_r, 7))
    else:
        print(-1)


solution()
