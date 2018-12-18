#  Problem from SPOJ
#  https://www.spoj.com/problems/PRO/


import heapq


def solution():

    n = int(input())
    sum_prizes = 0
    max_heap = []
    min_heap = []

    deleted_max = []
    deleted_min = []

    for i in range(n):
        line = list(map(int, input().strip().split()))
        num_rc = line[0]
        receipts = line[1:]
        for j in range(num_rc):
            heapq.heappush(min_heap, receipts[j])
            heapq.heappush(max_heap, -receipts[j])

        if len(max_heap) >= 2:
            from_max = heapq.heappop(max_heap)
            from_min = heapq.heappop(min_heap)
            while -from_max in deleted_min:
                pos = deleted_min.index(-from_max)
                deleted_min.pop(pos)
                from_max = heapq.heappop(max_heap)
            while -from_min in deleted_max:
                pos = deleted_max.index(-from_min)
                deleted_max.pop(pos)
                from_min = heapq.heappop(min_heap)

            deleted_max.append(from_max)
            deleted_min.append(from_min)

            sum_prizes -= (from_max + from_min)
            sum_prizes = sum_prizes % 1000000

    print(sum_prizes)


solution()
