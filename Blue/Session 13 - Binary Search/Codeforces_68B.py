# Problem from Codeforces
# http://codeforces.com/problemset/problem/68/B


def check_possibility(_accumulators, max_value, n, k):
    less = 0
    more = 0
    for i in range(n):
        if _accumulators[i] > max_value:
            more += _accumulators[i] - max_value
        else:
            less += max_value - _accumulators[i]

    return more - k * more / 100 >= less


def solution():
    n, k = map(int, input().strip().split())
    accumulators = list(map(int, input().strip().split()))

    lo = 0
    hi = 1000
    for i in range(100):
        mid = (lo + hi) / 2
        if check_possibility(accumulators, mid, n, k):
            lo = mid
        else:
            hi = mid

    print('{0:.9f}'.format(lo))


solution()


