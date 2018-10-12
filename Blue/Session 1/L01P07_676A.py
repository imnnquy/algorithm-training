# Problem from Codeforces
# http://codeforces.com/problemset/problem/676/A


def calc_max_dist(_a, _n):
    pos_min, pos_max = 0, 0
    for i in range(_n):
        if _a[i] == n:
            pos_max = i
        if _a[i] == 1:
            pos_min = i
    return max(n - 1 - pos_max, n - 1 - pos_min, pos_max, pos_min)


n = int(input())
a = list(map(int, input().split()))
print(calc_max_dist(a, n))
