#  Problem from UVA
#  https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1895


import heapq


def solution():
    while True:
        N = int(input())
        if N == 0:
            return
        array = list(map(int, input().strip().split()))
        heapq.heapify(array)
        sum = 0
        while len(array) > 1:
            first = heapq.heappop(array)
            second = heapq.heappop(array)
            sum += (first + second)
            heapq.heappush(array, first + second)

        print(sum)


solution()
