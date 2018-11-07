# Problem from Codeforces
# http://codeforces.com/problemset/problem/572/A


def check_arrays(_a, _b, _k, _m):
    if _a[k - 1] >= _b[-m]:
        return 'NO'
    else:
        return 'YES'


na, nb = map(int, input().split())
k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(check_arrays(a, b, k, m))
