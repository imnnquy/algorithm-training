# Problem from UVA
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=316&page=show_problem&problem=1552
# import sys

from bisect import bisect_right


def solution():
    N = int(input())
    lady_chimps = list(map(int, input().strip().split()))
    Q = int(input())
    queries = list(map(int, input().strip().split()))

    for q in queries:
        upper_bound = bisect_right(lady_chimps, q)
        shorter_index = -1
        if upper_bound > 0:
            for i in range(upper_bound - 1, -1, -1):
                if lady_chimps[i] < q:
                    shorter_index = i
                    break
        shorter = 'X'
        taller = 'X'
        if shorter_index != -1:
            shorter = str(lady_chimps[shorter_index])
        if upper_bound < N:
            taller = str(lady_chimps[upper_bound])

        print(shorter, taller)


solution()


