# Problem from Codeforces
# http://codeforces.com/problemset/problem/673/A


def calc_mins(_t, _n):
    if _t[0] > 15:
        return 15
    for i in range(1, _n):
        if _t[i] - _t[i - 1] > 15:
            return t[i - 1] + 15
    if 90 - _t[_n - 1] > 15:
        return _t[n - 1] + 15
    return 90


n = int(input())
t = list(map(int, input().split()))
print(calc_mins(t, n))
