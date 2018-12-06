#  Problem from Hackerrank
#  https://www.hackerrank.com/challenges/qheap1/problem

import heapq


def solution():
    Q = int(input())
    my_list = []
    delete_list = []
    for i in range(Q):
        query = input()
        if query.startswith('3'):
            while True:
                if my_list[0] not in delete_list:
                    break
                pos = delete_list.index(my_list[0])
                delete_list.pop(pos)
                heapq.heappop(my_list)

            print(my_list[0])
        else:
            command, param = map(int, query.split())
            if command == 1:
                heapq.heappush(my_list, param)
            else:
                delete_list.append(param)


solution()
