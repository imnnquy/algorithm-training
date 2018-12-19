#  Problem from SPOJ
#  https://www.spoj.com/problems/LAZYPROG/


import heapq


class Project:
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.d = d

    def __lt__(self, other):
        return True


def solution():
    t = int(input())
    sum_money = 0
    for i in range(t):
        n = int(input())
        for j in range(n):
            a, b, d = map(int, input().strip().split())

    print("{0:.2f}".format(sum_money))


solution()
