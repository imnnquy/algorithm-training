# Problem from SPOJ
# https://www.spoj.com/problems/EKO/


def check_possibility(_accumulators, max_value, n, k):

    total = 0
    for i in range(n):
        if _accumulators[i] > max_value:
            total += _accumulators[i] - max_value

    return total >= k


def solution():
    n, k = map(int, input().strip().split())
    trees = list(map(int, input().strip().split()))

    lo = 0
    hi = int(2e9)
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if check_possibility(trees, mid, n, k):
            lo = mid
        else:
            hi = mid

    print(lo)


solution()
