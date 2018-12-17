#  Problem from Hackerearth
#  https://www.hackerearth.com/fr/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/


import heapq


def solution():
    N = int(input())
    A = list(map(int, input().split()))

    if N < 3:
        print(-1)
        if N > 1:
            print(-1)
        return

    max_list = A[:3]
    heapq.heapify(max_list)

    for i in range(N):
        if i < 3:
            if i == 2:
                print(max_list[0]*max_list[1]*max_list[2])
            else:
                print(-1)
        else:
            if A[i] > max_list[0]:
                heapq.heappop(max_list)
                heapq.heappush(max_list, A[i])
            print(max_list[0]*max_list[1]*max_list[2])


solution()
