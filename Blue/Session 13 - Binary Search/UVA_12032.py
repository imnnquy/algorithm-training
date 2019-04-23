# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=31832
# import sys


def check_possibility(rungs, k, n):

    remain = k
    if rungs[0] > remain:
        return False
    if rungs[0] == remain:
        remain -= 1
    for i in range(1, n):
        if rungs[i] - rungs[i - 1] > remain:
            return False
        if rungs[i] - rungs[i-1] == remain:
            remain -= 1

    return remain >= 0


def solution():
    T = int(input())
    for i in range(T):
        N = int(input())
        rungs = list(map(int, input().strip().split()))

        lo = 0
        hi = int(1e7)
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check_possibility(rungs, mid, N):
                hi = mid
            else:
                lo = mid

        print('Case {0}: {1}'.format(i + 1, hi))


solution()

