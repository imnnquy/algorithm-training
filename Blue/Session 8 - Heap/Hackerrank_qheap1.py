#  Problem from Hackerrank
#  https://www.hackerrank.com/challenges/qheap1/problem


import heapq


def solution():
    Q = int(input())
    my_list = []
    for i in range(Q):
        query = input()
        if query.startswith('3'):
            print(my_list[0])
        else:
            command, param = map(int, query.split())
            if command == 1:
                heapq.heappush(my_list, param)
            else:
                for j in range(len(my_list)):
                    if my_list[j] == param:
                        my_list[j] = my_list[-1]
                        my_list.pop()
                        if j < len(my_list):
                            heapq.heapify(my_list)
                        break


solution()

